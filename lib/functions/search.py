from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Website

def search_for_entry(session, website_name):
    entry=session.query(Website).filter_by(website=website_name).first()
    print(f'Username: {entry.username} and Password: {entry.password} for {entry.website}')

def look_for_entry():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    search_entry=input('Website to search for: ')
    search=search_for_entry(session, search_entry)
    session.close()