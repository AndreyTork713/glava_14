import sqlite3


def main():
    conn = sqlite3.connect('Inventory.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                VALUES (10, 'Циркулярная Пила', 199.99)''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()