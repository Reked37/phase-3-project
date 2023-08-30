from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def change_an_entry(session, verify_username):
    choice_what_to_update= input('Do you want to update the website, username, or password? ').lower()

    if choice_what_to_update == 'username':
        new_username=input('New username: ')
        verify_username.username= new_username
        session.commit()
        print(f'Username has been updated to {new_username}!')
    elif choice_what_to_update == 'website':
        new_website=input('New website: ')
        verify_username.website.website= new_website
        session.commit()
        print(f'Website has been updated to {new_website}!')
    elif choice_what_to_update == 'password':
        new_password=input('New password: ')
        verify_username.password= new_password
        session.commit()
        print('Password has been updated!')
    else:
        print(f"Can not update '{choice_what_to_update}'")
        change_an_entry(session, verify_username)

def verify_user(session, lookup_username):
    verify_username= session.query(User).filter_by(username=lookup_username).first()

    if not verify_username:
        print(f'{lookup_username} was not found. Please try again.')
        look_in_database()
    else:
        print(f'Website: {verify_username.website.website} Username: {verify_username.username} and Password: {verify_username.password}')
        change_an_entry(session, verify_username)


def look_in_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    lookup_username=input('What user do you want to update? ')
    verify_user(session, lookup_username)
    session.close()


   