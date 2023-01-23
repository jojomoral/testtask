import sqlite3

from CONFIG import DATABASE_PATH


def create_tables():
    sql = """
CREATE TABLE regions (
id INTEGER PRIMARY KEY AUTOINCREMENT,
region_name TEXT
);

CREATE TABLE cities (
id INTEGER PRIMARY KEY AUTOINCREMENT,
region_id INTEGER,
city_name TEXT,
FOREIGN KEY (region_id) REFERENCES regions(id)
);
    
CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
second_name TEXT,
first_name TEXT,
patronymic TEXT,
region_id INTEGER,
city_id INTEGER,
phone TEXT,
email TEXT,
FOREIGN KEY (region_id) REFERENCES regions(id),
FOREIGN KEY (city_id) REFERENCES cities(id)
)
"""
    regions_data = ((0, "Краснодарский край"), (1, "Ростовская область"), (2, "Ставропольский край",))
    cities_data = (
        (0, 0, "Краснодар"),
        (1, 0, "Кропоткин"),
        (2, 0, "Славянск"),
        (3, 1, "Ростов"),
        (4, 1, "Шахты"),
        (5, 1, "Батайск"),
        (6, 2, "Ставрополь"),
        (7, 2, "Пятигорск"),
        (8, 2, "Кисловодск")
    )
    users_data = (
        ("Петров", "Петр", "Петрович", "0", "0", "+7 111 111 11 11", "petrov@mail.ru"),
        ("Иванов", "Иван", "Иванович", "0", "2", "+7 222 222 22 22", "ivanov@mail.ru"),
        ("Александров", "Александр", "Александрович", "2", "6", "+7 333 333 33 33", "alexandrov@mail.ru")
    )
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.executescript(sql)
        conn.commit()
    insert_region(regions_data)
    insert_city(cities_data)
    insert_user(users_data)


def insert_region(data):
    with sqlite3.connect(DATABASE_PATH) as conn:
        sql = "INSERT INTO regions (id, region_name) VALUES (?, ?)"
        conn.executemany(sql, data)
        conn.commit()


def insert_city(data):
    with sqlite3.connect(DATABASE_PATH) as conn:
        sql = "INSERT INTO cities (id, region_id, city_name) VALUES (?, ?, ?)"
        conn.executemany(sql, data)
        conn.commit()


def insert_user(data):
    with sqlite3.connect(DATABASE_PATH) as conn:
        sql = "INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)"
        conn.executemany(sql, data)
        conn.commit()


def get_users(region_city_names = False):
    with sqlite3.connect(DATABASE_PATH) as conn:
        curs = conn.cursor()
        if not region_city_names:
            sql = "SELECT * FROM users"
        else:
            sql = """
            SELECT users.id, second_name, first_name, patronymic, regions.region_name, cities.city_name, phone, email FROM users
INNER JOIN regions ON users.region_id = regions.id
INNER JOIN cities ON users.city_id = cities.id
            """
        curs.execute(sql)
        data = curs.fetchall()
        return data


def get_regions():
    with sqlite3.connect(DATABASE_PATH) as conn:
        curs = conn.cursor()
        sql = "SELECT * FROM regions"
        curs.execute(sql)
        data = curs.fetchall()
        return data


def get_cities():
    with sqlite3.connect(DATABASE_PATH) as conn:
        curs = conn.cursor()
        sql = "SELECT * FROM cities"
        curs.execute(sql)
        data = curs.fetchall()
        return data
