sqlite3


MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def main():
    choice = 0
    while choice is not EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()




def display_menu():
    pass

def get_menu_choice():
    pass

def create():
    pass

def read():
    pass

def update():
    pass

def delete():
    pass




if __name__ == '__main__':
    main()