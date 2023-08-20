from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Website

def create_new_entry(session):
    website=input('Name of website: ')
    username=input('Username: ')
    password=input('Password: ')

    new_entry=Website(website=website, username=username, password=password)
    session.add(new_entry)
    session.commit()
    return new_entry

def add_to_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()

    entry=create_new_entry(session)

    print("New entry created!")

    session.close()





