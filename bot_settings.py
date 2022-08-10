from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import sqlite3
import token
TOKEN = token.TOKEN    #open("token.txt", "r").readline()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

path_to_main_gif = 'resources/start_gif.gif'
sqlite_connection = sqlite3.connect('training_telegram_bot.db')


def create_database():
    cursor = sqlite_connection.cursor()
    cursor.execute("""CREATE TABLE sedentary_work_table
                        (description text,
                         image_path text)""")
    cursor.execute("""CREATE TABLE users
                        (user_id integer,
                         sedentary_work_exercise_number integer)""")
    sqlite_connection.commit()
    cursor.close()





def insert_data():
    sqlite_connection = sqlite3.connect('training_telegram_bot.db')
    cursor = sqlite_connection.cursor()
    sqlite_insert_blob_query = """INSERT INTO sedentary_work_table
                                      (description, image_path) VALUES (?, ?)"""
    for i in range(1,9):
        path = 'resources/'+str(i)+'.jpg'
        description = open('resources/'+str(i)+'.txt').read()
        # Преобразование данных в формат кортежа
        data_tuple = (description,path)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
    cursor.close()

