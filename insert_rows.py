import sqlite3


def main():

    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO INVENTORY(ItemName, Price)
    VALUES('Отвертка', 4.99), 
    ('Молоток', 12.99), 
    ('Плоскогубцы', 14.99), 
    ('Электродрель', NULL)''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()