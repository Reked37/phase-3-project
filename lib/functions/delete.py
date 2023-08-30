from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def delete_entry(session, user_to_delete):
    entry=session.query(User).filter_by(username=user_to_delete).first()
    confirmation= input(f'Are you sure you want to delete {entry.username}? (Y/N): ').lower
    
    if confirmation == 'y' or 'yes':
        session.delete(entry)
        session.commit()
        print(f'Website {entry.username} has been deleted')
    else:
        print('Entry was not found')
        delete_from_database()

def delete_from_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    user_to_delete=input('What user do you want deleted? ')
    deletion=delete_entry(session, user_to_delete)
    session.close()