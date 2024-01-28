import sqlite3


def main():
    again = 'д'

    conn = sqlite3.connect('Inventory.db')
    cur = conn.cursor()

    while again == 'д':
        item_name = input('Введите наименование товара: ')
        item_price = float(input('Введите цену товара: '))
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                    VALUES (?, ?)''',
                    (item_name, item_price))

        # Добавить ещё?
        again = input('Продолжить добавление позиций в таблицу? д/н: ')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()




