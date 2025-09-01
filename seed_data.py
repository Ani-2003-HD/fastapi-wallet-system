from sqlalchemy.orm import Session
from database import SessionLocal
import models

def seed_database():
    db = SessionLocal()
    
    # Sample users
    users_data = [
        {"name": "John Doe", "email": "john@example.com", "phone": "+1234567890"},
        {"name": "Jane Smith", "email": "jane@example.com", "phone": "+0987654321"},
        {"name": "Bob Johnson", "email": "bob@example.com", "phone": "+1122334455"},
        {"name": "Alice Brown", "email": "alice@example.com", "phone": "+5566778899"},
        {"name": "Charlie Wilson", "email": "charlie@example.com", "phone": "+9988776655"}
    ]
    
    try:
        # Check if users already exist
        existing_users = db.query(models.User).count()
        if existing_users > 0:
            print("Database already has users. Skipping seed.")
            return
        
        # Create users
        for user_data in users_data:
            user = models.User(**user_data)
            db.add(user)
        
        db.commit()
        print("Sample users created successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
