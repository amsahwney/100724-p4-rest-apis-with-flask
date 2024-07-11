#!/usr/bin/env python3

from config import app, db
from models import Politician, Scandal, Involvement
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        # write your seeds here!

        print("Seeding complete!")