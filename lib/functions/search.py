from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def search_for_entry(session, entered_username):
    entry=session.query(User).filter_by(username=entered_username).first()
    print(f'Username: {entry.username} and Password: {entry.password} for {entry.website_name}')

def look_for_entry():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    entered_username=input('What user are you looking for? ')
    search=search_for_entry(session, entered_username)
    session.close()