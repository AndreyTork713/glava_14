import sqlite3


def main():
    # Переменная управления циклом
    again = 'д'

    while again == 'д':
        # Получить ID товара, название и цену
        item_id = int(input('Введите ID товара: '))
        item_name = input('Введите наименование товара: ')
        price = float(input('Введите цену товара: '))

        # Добавить товар в базу данных
        add_item(item_id, item_name, price)

        # Добавить ещё одну?
        again = input('Добавить ещё одну позицию? д/н: ')


# функция add_item добавляет позицию в базу данных.
def add_item(item_id, item_name, price):
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                                                   VALUES (?, ?, ?)''',
                    (item_id, item_name, price))
        conn.commit()

    except sqlite3.Error as err:
        print(err)


    finally:
        # Закрыть соединение
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    main()