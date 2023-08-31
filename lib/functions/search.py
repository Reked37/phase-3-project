from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def search_for_entry(session, entered_username):
    all_entries=session.query(User).filter_by(username=entered_username).all()

    if not all_entries:
        print(f'{entered_username} not found. Please try again.')
        look_for_entry()
    else:
        [
            print(f'Username: {entry.username} and Password: {entry.password} for {entry.website.website}')
            for
            entry in all_entries
        ]

def look_for_entry():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    entered_username=input('What user are you looking for? ')
    if entered_username == 'back':
        return
    search=search_for_entry(session, entered_username)
    session.close()