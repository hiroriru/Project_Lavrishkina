'''
Приложение для туристического агентства ТУР. Таблица Турист должна
содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки, Стоимость
путевки
'''
import sqlite3

DB_NAME = 'turist.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Turist (
                "Код клиента" INTEGER PRIMARY KEY AUTOINCREMENT,
                "Клиент (Фамилия)" TEXT NOT NULL,
                Телефон TEXT,
                "Название страны" TEXT,
                Регион TEXT,
                "Продолжительность поездки" INTEGER,
                "Стоимость путевки" REAL
            )
        """)
    print("База данных и таблица 'Turist' готовы.")

def input_data():
    print("\n--- Ввод новых данных ---")
    surname = input("Введите фамилию клиента: ")
    phone = input("Введите телефон клиента: ")
    country = input("Введите название страны: ")
    region = input("Введите регион (или оставьте пустым): ") or None
    try:
        duration = int(input("Введите продолжительность поездки (в днях): "))
        cost = float(input("Введите стоимость путевки (в рублях): "))
    except ValueError:
        print("Ошибка: введите числовые значения для длительности и стоимости.")
        return

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Turist (
                    "Клиент (Фамилия)", Телефон, "Название страны", Регион,
                    "Продолжительность поездки", "Стоимость путевки"
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (surname, phone, country, region, duration, cost))
            conn.commit()
            print(f"Данные клиента {surname} успешно добавлены.")
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении в базу данных: {e}")

def search_data():
    print("\n--- Поиск ---")
    print("1. По фамилии клиента")
    print("2. По стране")
    print("3. По минимальной стоимости")
    choice = input("Выберите критерий (1-3): ")

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        if choice == '1':
            surname = input("Введите фамилию: ")
            cur.execute('SELECT * FROM Turist WHERE "Клиент (Фамилия)" LIKE ?', (f'%{surname}%',))
        elif choice == '2':
            country = input("Введите страну: ")
            cur.execute('SELECT * FROM Turist WHERE "Название страны" = ?', (country,))
        elif choice == '3':
            try:
                min_cost = float(input("Введите минимальную стоимость: "))
                cur.execute('SELECT * FROM Turist WHERE "Стоимость путевки" >= ?', (min_cost,))
            except ValueError:
                print("Неверный ввод для стоимости.")
                return
        else:
            print("Неверный выбор.")
            return

        results = cur.fetchall()
        if results:
            for row in results:
                print(f"Код: {row[0]}, Фамилия: {row[1]}, Страна: {row[3]}, Цена: {row[6]}")
        else:
            print("Записи не найдены.")

def delete_data():
    print("\n--- Удаление ---")
    print("1. По коду клиента")
    print("2. По фамилии клиента")
    print("3. По стране")
    choice = input("Выберите критерий (1-3): ")

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        param = None
        if choice == '1':
            try:
                param = int(input("Введите код клиента: "))
                cur.execute('DELETE FROM Turist WHERE "Код клиента" = ?', (param,))
            except ValueError:
                print("Неверный ввод для кода.")
                return
        elif choice == '2':
            param = input("Введите фамилию: ")
            cur.execute('DELETE FROM Turist WHERE "Клиент (Фамилия)" = ?', (param,))
        elif choice == '3':
            param = input("Введите страну: ")
            cur.execute('DELETE FROM Turist WHERE "Название страны" = ?', (param,))
        else:
            print("Неверный выбор.")
            return

        if cur.rowcount > 0:
            conn.commit()
            print(f"Удалено {cur.rowcount} записей.")
        else:
            print("Записи для удаления не найдены.")

def edit_data():
    print("\n--- Редактирование ---")
    tourist_id = input("Введите код клиента для редактирования: ")
    field = input("Какое поле изменить (Фамилия/Телефон/Страна/Регион/Длительность/Цена)? ")
    new_val = input(f"Введите новое значение для {field}: ")

    # Преобразуем поле в правильный столбец таблицы
    field_map = {
        "Фамилия": '"Клиент (Фамилия)"',
        "Телефон": "Телефон",
        "Страна": '"Название страны"',
        "Регион": "Регион",
        "Длительность": '"Продолжительность поездки"',
        "Цена": '"Стоимость путевки"'
    }
    column = field_map.get(field)
    if not column:
        print("Неверное имя поля.")
        return

    # Пытаемся преобразовать значение для числовых полей
    if field in ["Длительность", "Цена"]:
        try:
            new_val = float(new_val) if '.' in new_val else int(new_val)
        except ValueError:
            print("Неверный формат числа.")
            return

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(f'UPDATE Turist SET {column} = ? WHERE "Код клиента" = ?', (new_val, tourist_id))
        if cur.rowcount > 0:
            conn.commit()
            print("Данные обновлены.")
        else:
            print("Клиент с таким кодом не найден.")

init_db()

# Ввод 10 записей вручную пользователем
print("Введите 10 записей о клиентах.")
for i in range(10):
    print(f"\n--- Запись {i+1} ---")
    input_data()

# Цикл для выполнения операций пользователем
while True:
    print("\n--- Меню ---")
    print("1. Ввести нового клиента")
    print("2. Найти клиента")
    print("3. Удалить клиента")
    print("4. Редактировать клиента")
    print("5. Выйти")
    action = input("Выберите действие (1-5): ")

    if action == '1':
        input_data()
    elif action == '2':
        search_data()
    elif action == '3':
        delete_data()
    elif action == '4':
        edit_data()
    elif action == '5':
        break
    else:
        print("Неверный выбор.")