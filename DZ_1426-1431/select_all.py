import sqlite3


def main():
    # Установить соединение с базой данных
    conn = sqlite3.connect('inventory_1.db')

    # Получить курсор
    cur = conn.cursor()
    # Прописать курсору команду на выполнение (выбрать все данные таблицы и вывести их на печать)
    cur.execute('''SELECT * FROM Inventory_1''')
    # Присвоить переменной results результаты выполнения функции fetchall()
    results = cur.fetchall()
    # Вывести через цикл результаты на печать
    for row in results:
        print(f'{row[0]:3} {row[1]:5} {row[2]:3} {row[3]:5}')


if __name__=='__main__':
    main()
