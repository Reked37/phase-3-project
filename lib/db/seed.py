from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Website

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine)
session= Session()
fake=Faker()

def delete_table():
    session.query(Website).delete()

def create_records():
    websites=[Website(
        website= fake.name(),
        username= fake.name(),
        password= fake.name()
    ) for i in range(10)]

    session.add_all(websites)
    session.commit()
    return websites

if __name__ == '__main__':
    delete_table()
    websites = create_records()
