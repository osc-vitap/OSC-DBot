# Initializing database
import psycopg2
from os import getenv

DATABASE_URL = getenv("DB_URL")


def create_tables():
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    CREATE_TABLE_QUERY = """
    CREATE TABLE tempVariable (
        id SERIAL PRIMARY KEY,
        prefix VARCHAR(10) NOT NULL,
        event_id int NOT NULL,
        newsTimestamp VARCHAR(30) NOT NULL
    );
    """
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE_QUERY)
    conn.commit()
    conn.close()
    print("[!] DATABASE CREATED SUCCESSFULLY")


def insert_values():
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    INSERT_QUERY = """
    INSERT INTO tempVariable (id, prefix, event_id, newsTimestamp)
    VALUES (%s, %s, %s, %s);
    """
    cursor = conn.cursor()
    cursor.execute(INSERT_QUERY, (1, ">", 43, "12 Nov 2021 | 00:00 AM"))
    conn.commit()
    conn.close()
    print("[!] VALUES INSERTED SUCCESSFULLY")


def get_data(query):
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute(f"SELECT {query} FROM tempVariable;")
    result = cursor.fetchone()
    return result[0]


def update_data(query):
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tempVariable SET {query} WHERE id = 1;")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # create_tables()
    # insert_values()
    # print(get_data("id"))
    # print(get_data("prefix"))
    # print(get_data("event_id"))
    # print(get_data("newsTimestamp"))
    # update_data("event_id = '40'")
    print(get_data("event_id"))
