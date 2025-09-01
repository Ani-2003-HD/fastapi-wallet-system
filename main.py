from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine
from datetime import datetime, timezone

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Wallet Management System",
    description="A simple wallet management system with user and transaction APIs",
    version="1.0.0"
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Wallet Management System API"}

@app.get("/users", response_model=List[schemas.UserWithWallet], tags=["Users"])
def list_users(db: Session = Depends(get_db)):
    """
    Fetch all users with their wallet balance
    """
    users = db.query(models.User).all()
    result = []
    for user in users:
        wallet = db.query(models.Wallet).filter(models.Wallet.user_id == user.id).first()
        balance = wallet.balance if wallet else 0.0
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "wallet_balance": balance
        })
    return result

@app.put("/wallet/{user_id}", response_model=schemas.WalletResponse, tags=["Wallet"])
def update_wallet(user_id: int, wallet_update: schemas.WalletUpdate, db: Session = Depends(get_db)):
    """
    Add or update amount in user's wallet
    """
    # Check if user exists
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get or create wallet
    wallet = db.query(models.Wallet).filter(models.Wallet.user_id == user_id).first()
    if not wallet:
        wallet = models.Wallet(user_id=user_id, balance=0.0)
        db.add(wallet)
    
    # Update balance
    old_balance = wallet.balance
    wallet.balance += wallet_update.amount
    wallet.updated_at = datetime.now(timezone.utc)
    
    # Create transaction record
    transaction = models.Transaction(
        user_id=user_id,
        amount=wallet_update.amount,
        transaction_type="CREDIT" if wallet_update.amount > 0 else "DEBIT",
        description=wallet_update.description or f"Wallet update: {wallet_update.amount}",
        created_at=datetime.now(timezone.utc)
    )
    db.add(transaction)
    
    db.commit()
    db.refresh(wallet)
    
    return {
        "user_id": user_id,
        "old_balance": old_balance,
        "new_balance": wallet.balance,
        "amount_added": wallet_update.amount,
        "message": "Wallet updated successfully"
    }

@app.get("/transactions/{user_id}", response_model=List[schemas.TransactionResponse], tags=["Transactions"])
def fetch_transactions(user_id: int, db: Session = Depends(get_db)):
    """
    Fetch all wallet transactions for a specific user
    """
    # Check if user exists
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    transactions = db.query(models.Transaction).filter(
        models.Transaction.user_id == user_id
    ).order_by(models.Transaction.created_at.desc()).all()
    
    return transactions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
