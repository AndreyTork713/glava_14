import sqlite3


def main():
    conn = sqlite3.connect('inventory_dz2.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO inventory_dz2 (ItemID, ItemName, Price)
                VALUES (10, 'Циркулярная Пила', 199.99)''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()