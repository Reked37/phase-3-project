from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def verify_user(session, user_to_delete):
    verify_user=session.query(User).filter_by(username=user_to_delete).first()
    if not verify_user:
        print(f'{user_to_delete} was not found. Please try again.')
        delete_from_database()
    
    
    confirmation= input(f'Are you sure you want to delete {verify_user.username}? (Y/N): ').lower()
    if confirmation == 'y' or confirmation == 'yes':
        session.delete(verify_user)
        session.commit()
        print(f'{verify_user.username} has been deleted')
    else:
        delete_from_database()

def delete_from_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    user_to_delete=input('What user do you want deleted? ')
    if user_to_delete == 'back':
        return

    deletion=verify_user(session, user_to_delete)
    session.close()