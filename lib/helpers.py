from create import create_new_entry

def main_menu():
    print('Welcome to Password Manager aka P-Man')
    print("Type in 'Create' for new entry, 'Search' for password, 'Change' to modify an entry, or 'Delete' to delete an entry")
    
def decision(choice):
    decision= choice.lower()
    print(decision)
    if decision == 'create':
        create_new_entry()
    elif decision == 'search':
        print('searched')
    elif decision == 'change':
        print('changed')
    elif decision == 'delete':
        print('deleted')
    else:
        print(f'{choice} is not a valid choice')