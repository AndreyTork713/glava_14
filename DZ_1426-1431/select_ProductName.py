import sqlite3


def main():

    conn = sqlite3.connect('inventory_1.db')

    cur = conn.cursor()
    cur.execute('''SELECT ProductName FROM Inventory_1 WHERE ProductName LIKE "%t"''')
    res = cur.fetchall()
    for row in res:
        print(f'{row[0]:5}')


if __name__ == '__main__':
    main()