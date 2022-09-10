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
#TOKEN= '5403558275:AAE-oc5a_28rwwUfPwPfPqeEJa2q1dE7yrg'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

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




