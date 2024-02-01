import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    cur.execute('SELECT SUM(UnitsOnHand) FROM Products')
    res = cur.fetchone()[0]
    print(res)

    conn.close()


if __name__ == '__main__':
    main()