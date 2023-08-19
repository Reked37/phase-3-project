from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Website

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine)
session= Session()

def create_new_entry():
    website=input('Name of website: ')
    username=input('Username: ')
    password=input('Password: ')
    print(website, username, password)