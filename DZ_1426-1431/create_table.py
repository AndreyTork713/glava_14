import sqlite3


def main():
    conn = sqlite3.connect('inventory_1.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Inventory_1 (ItemID INTEGER PRIMARY KEY NOT NULL,
                ProductName TEXT, QtyHand INTEGER, Cost REAL)''')

    cur.execute('''INSERT INTO Inventory_1 (ProductName, QtyHand, Cost)
                VALUES ('Asdddss', 23, 12.3)''')

    cur.execute('SELECT * FROM Inventory_1')
    res = cur.fetchall()
    print(res)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()