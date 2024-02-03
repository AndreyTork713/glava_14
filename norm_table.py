import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    cur.execute('''SELECT Description from Products ORDER BY ProductID''')
    conn.close()


if __name__ == '__main__':
    main()
