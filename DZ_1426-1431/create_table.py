import sqlite3


def main():
    conn = sqlite3.connect('inventory_1.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Inventory_1 (ItemID INTEGER PRIMARY KEY NOT NULL,
    ProductName TEXT, QtyHand INTEGER, Cost REAL)''')
    cur.execute('''INSERT INTO Inventory_1 (ProductName, QtyHand, Cost) 
                VALUES ('asd', 12, 32.1), 
                       ('qwe', 54, 34.5), 
                       ('fgh', 45, 76.5), 
                       ('iuy', 57, 54.6), 
                       ('rnt', 66, 98.4)''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()

