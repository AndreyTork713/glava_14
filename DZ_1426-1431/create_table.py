import sqlite3


def main():
    conn = sqlite3.connect('inventory_1.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Inventory_1 (ItemID INTEGER PRIMARY KEY NOT NULL,
    ProductName TEXT, QtyHand INTEGER, Cost REAL)''')