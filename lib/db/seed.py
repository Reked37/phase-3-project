from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Website, User, WebsiteUser

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine)
session= Session()
fake=Faker()

def delete_table():
    session.query(Website).delete()
    session.query(User).delete()
    session.commit()

def create_records():
    websites=[Website(
        website= fake.name(),
        username= fake.name(),
        password= fake.name()
    ) for i in range(10)]
    users=[User(
        name_of_user=fake.name(),
        web_browser=fake.name()
    ) for i in range(10)]

    session.add_all(websites + users)
    session.commit()
    return websites, users

if __name__ == '__main__':
    delete_table()
    websites, users = create_records()
