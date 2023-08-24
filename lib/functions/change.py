from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User

def change_an_entry(session, lookup_username):
    info_to_change= session.query(User).filter_by(username=lookup_username).first()
    print(f'Website: {info_to_change.website_name} Username: {info_to_change.username} and Password: {info_to_change.password}')
    choice_what_to_update= input('What do you want updated? ').lower()

    if choice_what_to_update == 'username':
        new_username=input('New username: ')
        info_to_change.username= new_username
        session.commit()
        print(f'Username has been updated to {new_username}!')
    elif choice_what_to_update == 'website':
        new_website=input('New website: ')
        info_to_change.website_name= new_website
        session.commit()
        print(f'Website has been updated to {new_website}!')
    elif choice_what_to_update == 'password':
        new_password=input('New password: ')
        info_to_change.password= new_password
        session.commit()
        print('Password has been updated!')
    else:
        print(f"Can not update '{choice_what_to_update}'")


def look_in_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    lookup_username=input('What user do you want to update? ')
    change_an_entry(session, lookup_username)
    session.close()


   