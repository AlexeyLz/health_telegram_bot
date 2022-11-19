from aiogram import Bot
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
import sqlite3
import os
from dotenv import load_dotenv, find_dotenv
import urllib.parse as up
import psycopg2

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)





path_to_main_gif = 'resources/start_gif.gif'
path_to_main_logo = 'resources/logo.png'
path_to_main_logo_jpg = 'resources/logo.jpg'

path_to_db_bot = os.getenv('path_to_db_bot')

up.uses_netloc.append("postgres")
url = up.urlparse(path_to_db_bot)
connection = psycopg2.connect(database=url.path[1:],
                              user=url.username,
                              password=url.password,
                              host=url.hostname,
                              port=url.port)
