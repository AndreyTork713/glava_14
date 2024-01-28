import sqlite3


def main():
    conn = sqlite3.connect('Inventory.db')
    cur = conn.cursor()
    cur.execute('''DROP TABLE Inventory''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()