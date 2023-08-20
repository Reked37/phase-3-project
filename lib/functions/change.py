from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Website

def change_an_entry(session, website_input):
    info_to_change= session.query(Website).filter_by(website=website_input).first()
    print(f'Website: {info_to_change.website} Username: {info_to_change.username} and Password: {info_to_change.password}')
    choice_what_to_update= input('What do you want updated? ').lower()

    if choice_what_to_update == 'username':
        new_username=input('New username: ')
        info_to_change.username= new_username
        session.commit()
        print(f'Username has been updated to {new_username}!')
    elif choice_what_to_update == 'website':
        new_website=input('New website: ')
        info_to_change.website= new_website
        session.commit()
        print(f'Website has been updated to {new_website}!')
    elif choice_what_to_update == 'password':
        new_password=input('New password: ')
        info_to_change.password= new_password
        session.commit()
        print('Username has been updated!')
    else:
        print(f"Can not update '{choice_what_to_update}'")


def look_in_database():
    engine=create_engine('sqlite:///projectdatabase.db')
    Session= sessionmaker(bind=engine) 
    session= Session()

    website_input=input('Website you want updated: ')
    change_an_entry(session, website_input)
    session.close()


   