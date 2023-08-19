def main_menu(choice):
    print('Welcome to Password Manager aka P-Man')
    print("Type in 'Create' for new entry, 'Search' for password, 'Change' to modify an entry, or 'Delete' to delete an entry")
    decision= choice.lower()
    print(decision)
    if decision == 'create':
        print('created')
    elif decision == 'search':
        print('searched')
    elif decision == 'change':
        print('changed')
    elif decision == 'delete':
        print('deleted')
    else:
        print(f'{choice} is not a valid choice')