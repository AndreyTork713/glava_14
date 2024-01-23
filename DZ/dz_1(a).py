import sqlite3


def main():
    # 1/5
    conn = sqlite3.connect('dz_1.db')
    # 2/5
    cur = conn.cursor()

    # 3/5
    cur.execute('''DROP TABLE IF EXISTS Book''')

    # 4/5
    conn.commit()
    # 5/5
    conn.close()


if __name__ == '__main__':
    main()