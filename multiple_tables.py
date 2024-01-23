import sqlite3


def main():

    # 1/5
    conn = sqlite3.connect('company.db')

    # 2/5
    cur = conn.cursor()

    # 3/5
    # 3a Таблица КЛИЕНТЫ
    cur.execute('''CREATE TABLE IF NOT EXISTS Customers (CustomerID INTEGER PRIMARY KEY NOT NULL,
    Name TEXT, Email TEXT)''')
    # 3b Таблица СЛУЖАЩИЕ
    cur.execute('''CREATE TABLE IF NOT EXISTS Employees (EmployeeID INTEGER PRIMARY KEY NOT NULL,
    Name TEXT, Position TEXT)''')
    cur.execute('''DROP TABLE IF EXISTS Temp''')

    # 4/5
    conn.commit()
    # 5/5
    conn.close()


if __name__ == '__main__':
    main()

