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
FOREIGN KEY (region_id) REFERENCES regions(id),
FOREIGN KEY (city_id) REFERENCES cities(id)
)
"""
    regions_data = (("Краснодарский край",), ("Ростовская область",), ("Ставропольский край",))
    cities_data = (
        (0, "Краснодар"),
        (0, "Кропоткин"),
        (0, "Славянск"),
        (1, "Ростов"),
        (1, "Шахты"),
        (1, "Батайск"),
        (2, "Ставрополь"),
        (2, "Пятигорск"),
        (2, "Кисловодск")
    )
    users_data = (
        ("Петров", "Петр", "Петрович", "0", "0"),
        ("Иванов", "Иван", "Иванович", "0", "2"),
        ("Александров", "Александр", "Александрович", "2", "6")
    )
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.executescript(sql)
        conn.commit()
    insert_regions(regions_data)
    insert_cities(cities_data)
    insert_users(users_data)


def insert_regions(data):
    with sqlite3.connect(DATABASE_PATH) as conn:
        sql = "INSERT INTO regions (region_name) VALUES (?)"
        conn.executemany(sql, data)
        conn.commit()

def insert_cities(data):
    with sqlite3.connect(DATABASE_PATH) as conn:
        sql = "INSERT INTO cities (region_id, city_name) VALUES (?, ?)"
        conn.executemany(sql, data)
        conn.commit()

def insert_users(data):
    with sqlite3.connect(DATABASE_PATH) as conn:
        sql = "INSERT INTO users (second_name, first_name, patronymic, region_id, city_id) VALUES (?, ?, ?, ?, ?)"
        conn.executemany(sql, data)
        conn.commit()
