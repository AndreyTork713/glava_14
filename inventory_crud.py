import sqlite3


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


# функция выводит на экран главное меню
def display_menu():
    print('\n-----Меню ведения учета инструментов-----')
    print('1. Создать новую позицию')
    print('2. Прочитать позицию')
    print('3. Обновить позицию')
    print('4. Удалить позицию')
    print('5. Выйти из программы')


# функция получает от пользователя выбранный пункт меню
def get_menu_choice():
    choice = int(input('Введите ваш вариант: '))
    # Проверить входные данные
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант: '))
    return choice






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