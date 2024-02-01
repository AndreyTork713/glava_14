import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    cur.execute('SELECT SUM(UnitsOnHand) FROM Products')
    res1 = cur.fetchone()[0]
    cur.execute('SELECT MIN(RetailPrice) FROM Products')
    res2 = cur.fetchone()[0]
    print(res1, res2)

    conn.close()


if __name__ == '__main__':
    main()