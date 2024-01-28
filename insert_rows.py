import sqlite3


def main():
    conn = sqlite3.connect('Inventory.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO inventory (ItemName, Price)
    VALUES ('Отвертка', '3.44'),
           ('Плоскогубцы', '125.52'),
           ('Паяльник', '235.45'),
           ('Болгарка', '1545.99')''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()