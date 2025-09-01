from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    phone: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserWithWallet(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    wallet_balance: float

    class Config:
        from_attributes = True

class WalletUpdate(BaseModel):
    amount: float
    description: Optional[str] = None

class WalletResponse(BaseModel):
    user_id: int
    old_balance: float
    new_balance: float
    amount_added: float
    message: str

    class Config:
        from_attributes = True

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    transaction_type: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True
