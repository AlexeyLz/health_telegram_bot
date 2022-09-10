import asyncio

from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.utils import executor
from bot_settings import bot, dp, path_to_main_gif, connection, WEBHOOK_HOST, WEBHOOK_PATH
from red_button import start_menu
import bot_texts as bt


import logging


from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook




WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 8443

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')







def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="🔴", callback_data="start_state_1"),
               types.InlineKeyboardButton(text="🔵", callback_data="start_state_2"),
               types.InlineKeyboardButton(text="❔", callback_data="start_state_3"),
               ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def save_user(user_id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id =%s', (str(user_id),))
    entry = cursor.fetchone()

    if entry is None:
        cursor.execute('INSERT INTO users VALUES(' + str(user_id) + ',0)')

    connection.commit()
    cursor.close()


@dp.message_handler(commands="start")
async def console_start(message: types.Message):
    await cmd_start(message)
    print(message.from_user.id)
    save_user(message.from_user.id)


async def cmd_start(message: types.Message):
    button_to_start = types.KeyboardButton(bt.back_to_start)
    to_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_to_start)
    photo = open(path_to_main_gif, 'rb')
    me = await bot.get_me()
    name_bot = me.first_name
    txt = 'Привет, ' + str(message.from_user.first_name) + \
          '\nДобро пожаловать в ' + str(name_bot) + bt.main_text

    await message.answer_animation(animation=photo, reply_markup=to_start_keyboard)
    await message.answer(txt, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="start_state"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":

        await call.message.delete()

        await start_menu.menu(call.message)
    elif action == "2":

        await call.message.delete()

        print(2)

    elif action == "3":

        await call.message.delete()

        await process_help_command(call.message)


@dp.message_handler(Text(equals=bt.back_to_start))
async def with_puree(message: types.Message):
    await cmd_start(message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(bt.hello_text)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, bt.do_not_understand)


if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=True, on_startup=console_start)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
