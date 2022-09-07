from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import sqlite3
import os
from dotenv import load_dotenv, find_dotenv
import urllib.parse as up
import psycopg2

#load_dotenv(find_dotenv())

#TOKEN = os.getenv('TOKEN')
TOKEN1 = '5403558275:AAE-oc5a_28rwwUfPwPfPqeEJa2q1dE7yrg'
bot = Bot(token=TOKEN1)
dp = Dispatcher(bot)

path_to_main_gif = 'resources/start_gif.gif'

#path_to_db_bot = os.getenv('path_to_db_bot')
path_to_db_bot = 'postgres://fmmpoivj:U939QIpG1RAQj4C-IqHlIt7ai7Tx3B0O@abul.db.elephantsql.com/fmmpoivj'
up.uses_netloc.append("postgres")
url = up.urlparse(path_to_db_bot)
connection = psycopg2.connect(database=url.path[1:],
                              user=url.username,
                              password=url.password,
                              host=url.hostname,
                              port=url.port)


def create_database():
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sedentary_work_table
                        (serial_id SERIAL,
                         id INT,
                         description TEXT,
                         image_path TEXT)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                        (
                         user_id INTEGER,
                         serial_id SERIAL,
                         sedentary_work_exercise_number INTEGER)""")
    connection.commit()
    cursor.close()



def insert_data():

    cursor = connection.cursor()
    postgres_insert_blob_query = """INSERT INTO sedentary_work_table
                                      (id, description, image_path) VALUES (%s, %s, %s)"""
    for i in range(1, 9):
        path = 'resources/' + str(i) + '.jpg'
        description = open('resources/' + str(i) + '.txt').read()
        # Преобразование данных в формат кортежа
        data_tuple = (i, description, path)
        cursor.execute(postgres_insert_blob_query, data_tuple)
        connection.commit()
    cursor.close()

