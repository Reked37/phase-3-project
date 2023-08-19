from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Website

def delete_entry(session, website_name):
    # website_name=input('Website you want deleted: ')
    entry=session.query(Website).filter_by(website=website_name).first()
    print(entry.website)
    if entry:
        session.delete(entry)
        session.commit()
        print(f'Website {entry.website} has been deleted')
    else:
        print('Entry was not found')

def delete_from_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    website_to_delete=input('Website you want deleted: ')
    deletion=delete_entry(session, website_to_delete)
    session.close()