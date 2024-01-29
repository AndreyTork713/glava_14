import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Products')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:2} {row[1]:35} {row[2]:5} {row[3]:6} {row[4]:5}')

    conn.close()


if __name__ == '__main__':
    main()