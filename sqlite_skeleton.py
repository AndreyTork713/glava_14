import sqlite3


def main():
    # 1.Создать соединение с базой данных
    conn = sqlite3.connect('contacts.db')

    # 2.Создать курсор
    cur = conn.cursor()

    # Здесь вставить код для выполнения операций с базой данных

    # 3.Закоммитить изменения в базе данных
    conn.commit()

    # 4.Закрыть соединение с базой данных
    conn.close()


if __name__ == '__main__':
    main()

