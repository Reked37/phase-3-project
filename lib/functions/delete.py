from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Website

engine=create_engine('sqlite:///projectdatabase.db')
Session= sessionmaker(bind=engine) 
session= Session()

def delete_entry(session):
    website=input('Website you want deleted: ')
    entry=session.query(Website).filter_by(website).first()

    if entry:
        session.delete(entry)
        session.commit()
        return True
    else:
        return False

def delete_from_database():