import sqlite3

def main():
    # Переменная управления циклом
    again = 'д'

    # 1/5
    conn = sqlite3.connect('inventory.db')

    cur = conn.cursor()

    while again == 'д':
        # Получить название и цену позиции
        item_name = input('Название: ')
        price = float(input('Цена: '))

        # Добавить позицию в таблицу Inventory.
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                        VALUES (?, ?)''',
                    (item_name, price))

        # Добавить ещё?


