import sqlite3

CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

MIN_CHOICE = 1
MAX_CHOICE = 5

def main():
    choice = 0
    while choice is not EXIT:
        display_menu()
        choice = get_menu_choice()

        # ЭЛЕМЕНТЫ CRUD
        if choice == CREATE:
            create()
        if choice == READ:
            read()
        if choice == UPDATE:
            update()
        if choice == DELETE:
            delete()



# ФУНКЦИИ
def display_menu():
    print('Главное меню программы.')
    print('------------------------------')
    print('Создать новую таблицу      - 1')
    print('Записать данные в таблицу  - 2')
    print('Обновить данные в таблице  - 3')
    print('Удалить данные из таблицы  - 4')
    print('Создать новую таблицу      - 5')


def get_menu_choice():
    choice = input('Выберете пункт меню: ')
    return choice


# CRUD
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