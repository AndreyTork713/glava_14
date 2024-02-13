import sqlite3


def main():

    again = 'д'

    conn = sqlite3.connect('chocolate.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Products_test (ProductID INTEGER PRIMARY KEY NOT NULL,
    Description TEXT, UnitCost REAL, RetailPrice REAL, UnitsOnHand INTEGER)''')
    while again == 'д':
        item_description = input('Введите описание изделия: ')
        item_unit_cost = float(input('Введите стоимость единицы изделия: '))
        item_retail_price = float(input('Введите розничную цену изделия: '))
        item_units_on_hand = int(input('Введите количество единиц изделия в наличии: '))
        cur.execute('''INSERT INTO Products_test (Description, UnitCost, RetailPrice, UnitsOnHand) 
                VALUES (?, ?, ?, ?)''',
                (item_description, item_unit_cost, item_retail_price, item_units_on_hand))

        again = input('Продолжить заполнение таблицы? д/н: ')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()





