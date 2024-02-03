import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    cur.execute('''UPDATE Products
                    SET RetailPrice = 15
                    WHERE Description LIKE "%шоколада"''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()