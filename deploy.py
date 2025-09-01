#!/usr/bin/env python3
"""
Deployment script to initialize database and seed data
"""
import os
import sys
from database import engine
import models
from seed_data import seed_database

def main():
    print("🚀 Initializing database...")
    
    # Create all tables
    models.Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")
    
    # Seed the database
    print("🌱 Seeding database with sample data...")
    seed_database()
    print("✅ Database seeded successfully")
    
    print("🎉 Deployment initialization complete!")

if __name__ == "__main__":
    main()
