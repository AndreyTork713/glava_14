import sqlite3


def main():
    # 1/5
    conn = sqlite3.connect('dz_1.db')

    # 2/5

    cur = conn.cursor()

    # 3/5

    cur.execute('''CREATE TABLE IF NOT EXISTS Book (Код ISBN INTEGER PRIMARY KEY NOT NULL,
    Название издателя TEXT, Имя автора TEXT, Число страниц INTEGER NOT NULL)''')

    # 4/5
    conn.commit()

    # 5/5
    conn.close()

    
if __name__ == '__main__':
    main()