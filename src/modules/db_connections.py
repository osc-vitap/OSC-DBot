import psycopg2
from os import getenv

DATABASE_URL = getenv("DB_URL")


def get_data(query):
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute(f"SELECT {query} FROM tempVariable;")
    result = cursor.fetchone()
    return result[0]


def update_prefix(query):
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tempVariable SET prefix = '{query}' WHERE id = 1;")
    conn.commit()
    conn.close()


def update_newsTimestamp(query):
    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    cursor.execute(f"UPDATE tempVariable SET newsTimestamp = '{query}' WHERE id = 1;")
    conn.commit()
    conn.close()
