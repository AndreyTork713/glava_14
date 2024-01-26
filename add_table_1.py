import sqlite3


def main():
    conn = sqlite3.connect('Inventory.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
    ItemName TEXT NOT NULL, Price REAL NOT NULL)''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()