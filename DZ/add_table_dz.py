import sqlite3


def main():

    # item_ID = int(input('Введите ID объекта: '))
    item_Name = input('Введите наименование объекта: ')
    item_Price = float(input('Введите стоимость объекта: '))

    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Inventory (ItemId INTEGER PRIMARY KEY NOT NULL,
                    ItemName TEXT NOT NULL, Price REAL NOT NULL)''')
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                VALUES (?, ?)''',
                (item_Name, item_Price))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
