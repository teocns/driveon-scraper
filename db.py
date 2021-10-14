import json
from helpers import get_sql
from config import ATTRIBUTES_TO_SAVE, DB_HOST, DB_PASSWORD, DB_TABLENAME, DB_NAME, DB_USER, JSON_ATTRIBUTES_TO_SAVE
import psycopg2

connection = psycopg2.connect(
    database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=5432)


def init():
    # create table if it does not exist
    sql = get_sql("create_table")
    sql = sql.replace("<TABLE_NAME>", DB_TABLENAME)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    print("SQL initialized successfully")


def save_coche(coche: dict):
    cursor = connection.cursor()
    insert_row = {}

    query = "INSERT INTO %s (" % DB_TABLENAME
    NUM_OF_ATTRIBS = 0

    for attrib in ATTRIBUTES_TO_SAVE + JSON_ATTRIBUTES_TO_SAVE:
        val = coche.get(attrib, '')
        insert_row[attrib] = val if attrib not in JSON_ATTRIBUTES_TO_SAVE else json.dumps(
            val)
        query += "%s, " % attrib
        NUM_OF_ATTRIBS += 1

    query = query[:-2] + ") VALUES ("

    for i in range(NUM_OF_ATTRIBS):
        query += "%s, "

    query = query[:-2] + ") ON CONFLICT (oid) DO NOTHING;"

    # Insert row into database

    res = cursor.execute(query, tuple(insert_row.values()))
    connection.commit()

# init()
