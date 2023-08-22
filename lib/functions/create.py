from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Website

def create_new_entry(session, website_name, username, password):
    valid_website=session.query(Website).filter_by(website=website_name).first()
    #dictionary
    new_entry={'website_name': website_name, 'username': username, 'password': password, 'website_id':valid_website.id}
    session.add(User(**new_entry))
    session.commit()
    return new_entry

def add_to_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine)
    session= Session()

    website_name=input('Name of website: ')
    username=input('Username: ')
    password=input('Password: ')

    entry=create_new_entry(session, website_name, username, password)

    print("New entry created!")

    session.close()





