from functions.create import add_to_database
from functions.delete import delete_from_database

def main_menu():
    print('Welcome to Password Manager aka P-Man')
    print("Type in 'Create' for new entry, 'Search' for password, 'Change' to modify an entry, or 'Delete' to delete an entry")
    
def decision(choice):
    decision= choice.lower()
    print(decision)
    if decision == 'create':
        add_to_database()
    elif decision == 'search':
        print('searched')
    elif decision == 'change':
        print('changed')
    elif decision == 'delete':
        delete_from_database()
    else:
        print(f'{choice} is not a valid choice')