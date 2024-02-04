import sqlite3


def main():

    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    again = 'д'

    while again == 'д':
        pid = int(input('Введите ID изделия: '))
        cur.execute('''SELECT ProductID FROM Products''')
        len_table = len(cur.fetchall())
        if pid <= len_table:
            cur.execute('''SELECT Description, RetailPrice FROM Products WHERE ProductID == ?''', (pid,))
            res_1 = cur.fetchone()
            if res_1 is not None:
                print(f'Текущая цена изделия "{res_1[0]}": {res_1[1]:.2f}')
                new_price = float(input('Введите новую цену изделия: '))
                cur.execute('''UPDATE Products
                                SET RetailPrice = ?
                                WHERE ProductID = ?''',
                            (new_price, pid))
                conn.commit()
                print('Цена изделия изменена.')
            cur.execute('''SELECT Description, RetailPrice FROM Products WHERE ProductID == ?''', (pid,))
            res_2 = cur.fetchone()
            print(f'Новая цена изделия "{res_2[0]}": {res_2[1]:.2f}')
        else:
            print('Вы вышли за пределы значений таблицы!')

        again = input('Продолжить работу с таблицей? д/н:  ')

    conn.close()


if __name__ == '__main__':
    main()