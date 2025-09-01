# Wallet Management System

A simple FastAPI-based wallet management system with user and transaction APIs.

## Features

- **List Users API** - Fetch all users with their wallet balance
- **Update Wallet API** - Add or update amount in user's wallet
- **Fetch Transactions API** - Get all transactions for a specific user
- **Swagger Documentation** - Interactive API documentation

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd amrr_backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the seed script to populate sample data:
```bash
python seed_data.py
```

4. Start the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

### Swagger UI
Access the interactive API documentation at: `http://localhost:8000/docs`

### Available Endpoints

#### 1. List Users
- **GET** `/users`
- Returns all users with their wallet balance
- Response includes: id, name, email, phone, wallet_balance

#### 2. Update Wallet
- **PUT** `/wallet/{user_id}`
- Updates user's wallet balance
- Request body:
  ```json
  {
    "amount": 100.0,
    "description": "Payment received"
  }
  ```
- Response includes: old_balance, new_balance, amount_added

#### 3. Fetch Transactions
- **GET** `/transactions/{user_id}`
- Returns all transactions for a specific user
- Response includes: transaction details with amount, type, description, timestamp

## Database Schema

- **Users**: id, name, email, phone, created_at, updated_at
- **Wallets**: id, user_id, balance, created_at, updated_at
- **Transactions**: id, user_id, amount, transaction_type, description, created_at

## Testing the APIs

1. **List all users:**
```bash
curl http://localhost:8000/users
```

2. **Update wallet for user 1:**
```bash
curl -X PUT "http://localhost:8000/wallet/1" \
  -H "Content-Type: application/json" \
  -d '{"amount": 100.0, "description": "Initial deposit"}'
```

3. **Get transactions for user 1:**
```bash
curl http://localhost:8000/transactions/1
```

## Project Structure

```
amrr_backend/
├── main.py              # FastAPI application
├── database.py          # Database configuration
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── seed_data.py         # Sample data population
├── requirements.txt     # Dependencies
├── README.md           # Documentation
└── wallet_system.db    # SQLite database
```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server

## License

This project is open source and available under the MIT License.
