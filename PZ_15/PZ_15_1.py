'''
Приложение для туристического агентства ТУР. Таблица Турист должна
содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
путевки
'''
import sqlite3 as sq
from data import initial_records 

def init_db():
    """Создает таблицу и вставляет 10 позиций, если таблица пуста."""
    with sq.connect("tourism.db") as con:
        cur = con.cursor()
        # Создаем таблицу
        cur.execute("""CREATE TABLE IF NOT EXISTS tourists(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_surname TEXT NOT NULL,
            phone TEXT NOT NULL,
            country TEXT NOT NULL,
            region TEXT NOT NULL,
            trip_duration INTEGER NOT NULL,
            tour_cost REAL NOT NULL
        )""")
        
        cur.execute("SELECT COUNT(*) FROM tourists")
        count = cur.fetchone()[0]
        
        if count == 0:
            cur.executemany("INSERT INTO tourists(client_surname, phone, country, region, trip_duration, tour_cost) VALUES (?, ?, ?, ?, ?, ?)", initial_records)
            print("Таблица создана и заполнена 10 начальными позициями.")
        else:
            print(f"Таблица уже содержит {count} записей. Инициализация пропущена.")

def insert_data():
    with sq.connect("tourism.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM tourists") 
        cur.executemany("INSERT INTO tourists(client_surname, phone, country, region, trip_duration, tour_cost) VALUES (?, ?, ?, ?, ?, ?)", initial_records)
        print("Данные успешно перезаписаны (введено 10 позиций).")

def search_db():
    with sq.connect("tourism.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tourists WHERE client_surname LIKE 'Иванов%'")
        print("Поиск по фамилии 'Иванов%':")
        print(list(map(lambda x: f"ID:{x[0]} | {x[1]} | {x[2]} | {x[3]} | {x[4]} | {x[5]} дней | {x[6]} руб.", cur.fetchall())))
        
        cur.execute("SELECT * FROM tourists WHERE country = 'Турция'")
        print("\nПоиск по стране 'Турция':")
        print(list(map(lambda x: f"ID:{x[0]} | {x[1]} | {x[2]} | {x[3]} | {x[4]} | {x[5]} дней | {x[6]} руб.", cur.fetchall())))
        
        cur.execute("SELECT * FROM tourists WHERE tour_cost BETWEEN 40000 AND 70000")
        print("\nПоиск по стоимости от 40000 до 70000:")
        print(list(map(lambda x: f"ID:{x[0]} | {x[1]} | {x[2]} | {x[3]} | {x[4]} | {x[5]} дней | {x[6]} руб.", cur.fetchall())))

def delete_db():
    with sq.connect("tourism.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM tourists WHERE id = 3")
        cur.execute("DELETE FROM tourists WHERE tour_cost < 30000")
        cur.execute("DELETE FROM tourists WHERE country = 'Таиланд'")
        print("Удаление выполнено.")

def edit_db():
    with sq.connect("tourism.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE tourists SET tour_cost = tour_cost * 1.1 WHERE id = 2")
        cur.execute("UPDATE tourists SET region = 'Санкт-Петербург' WHERE country = 'Россия' AND region = 'Сочи'")
        cur.execute("UPDATE tourists SET trip_duration = trip_duration + 2 WHERE country = 'Египет'")
        print("Редактирование выполнено.")

def show_all():
    with sq.connect("tourism.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tourists")
        print("\nВсе записи")
        print(f"{'ID':<5} {'Дата':<12} {'Код':<8} {'Наименование':<25} {'Расходы':<15} {'Сумма':>10}")
        print("-" * 80)
        for row in cur.fetchall():
            print(f"{row[0]:<5} {row[1]:<12} {row[2]:<8} {row[3]:<25} {row[4]:<15} {row[5]:>10}")

def main():
    print("Запуск приложения 'ТУР'")
    init_db()
    
    while True:
        print("\n1. Ввод данных (10 позиций)")
        print("2. Поиск")
        print("3. Удаление")
        print("4. Редактирование")
        print("5. Просмотр всех")
        print("0. Выход")
        choice = input("Выбор: ")
        if choice == "1": insert_data()
        elif choice == "2": search_db()
        elif choice == "3": delete_db()
        elif choice == "4": edit_db()
        elif choice == "5": show_all()
        elif choice == "0": break
        else: print("Неверный выбор.")

if __name__ == "__main__":
    try:
        main()
    except sq.Error as e:
        print("Ошибка БД: " + str(e))
    except Exception as e:
        print("Ошибка: " + str(e))
