import sqlite3


def main():
    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()

    min_price = float(input('Введите минимальную цену: '))

    cur.execute('''SELECT Description, RetailPrice from Products WHERE RetailPrice >= ? ORDER BY RetailPrice''',
                (min_price,))

    # Извлекаем результаты
    results = cur.fetchall()

    if len(results) > 0:
        print('Вот результаты: ')
        print()
        print('Описание                      Цена')
        print('-------------------------------------')
        for row in results:
            print(f'{row[0]:30} {row[1]:>5}')
    else:
        print('Ни одно изделие не найдено')

    cur.execute('''SELECT Description FROM Products WHERE Description LIKE "%горячего%"''')
    res = cur.fetchall()
    for item in res:
        print(item)

    conn.close()


if __name__ == '__main__':
    main()


