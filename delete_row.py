import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    print('Эта программа удаляет строки из таблицы')
    again = 'д'
    while again == 'д':
        cur.execute('''SELECT ProductID FROM Products''')
        len_table = len(cur.fetchall())
        print(f'Длина таблицы {len_table} позиций')
        pid = int(input('Введите ID позиции для удаления: '))

        if pid <= len_table:
            cur.execute('''DELETE FROM Products WHERE ProductID == ?''', (pid,))

            conn.commit()
            print('Позиция удалена из таблицы.')
            print(cur.rowcount)

        else:
            print('Вы вышли за пределы значений таблицы.')

        again = input('Вы хотите продолжить? д/н: ')
    conn.close()


if __name__ == '__main__':
    main()