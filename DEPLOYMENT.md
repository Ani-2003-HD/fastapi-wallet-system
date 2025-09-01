# Deployment Guide

## Option 1: Railway (Recommended - Free)

1. Go to [Railway.app](https://railway.app) and sign up/login
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub account and select `fastapi-wallet-system`
4. Railway will automatically detect it's a Python app and deploy
5. Your app will be available at the provided URL

## Option 2: Render (Free)

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New" → "Web Service"
3. Connect your GitHub account and select `fastapi-wallet-system`
4. Configure:
   - **Name**: fastapi-wallet-system
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"

## Option 3: Heroku (Free tier discontinued, but still popular)

1. Install Heroku CLI: `brew install heroku/brew/heroku`
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku master`

## Local Testing

Before deploying, test locally:
```bash
pip install -r requirements.txt
python seed_data.py
python main.py
```

Visit: http://localhost:8000/docs for Swagger UI

## Environment Variables

The app will work with default SQLite database. For production, you can add:
- `DATABASE_URL`: PostgreSQL connection string (optional)
- `PORT`: Port number (auto-set by hosting platform)
