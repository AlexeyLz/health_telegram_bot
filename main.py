import os

import aiogram
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.utils import executor
import logging
import commands
import languages
from bot_settings import bot, dp, path_to_main_gif, connection, path_to_main_logo, path_to_main_logo_jpg
from red_button import start_menu
import bot_texts as bt
from aiogram.utils.executor import start_webhook


def get_start_keyboard():
    buttons = [types.InlineKeyboardButton(text="💪 Упражнения 💪", callback_data="start_state_1"),
               types.InlineKeyboardButton(text="🌍 Языки 🌍", callback_data="start_state_2"),
               #types.InlineKeyboardButton(text="⏰ Расписание ⏰", callback_data="start_state_3"),
               types.InlineKeyboardButton(text="ℹ️ Информация ℹ️", callback_data="start_state_4"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def save_user(user_id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id =%s', (str(user_id),))
    entry = cursor.fetchone()
    if entry is None:
        cursor.execute('INSERT INTO users VALUES(' + str(user_id) + ',0,0)')
    connection.commit()
    cursor.close()


async def start_bot(message: types.Message):
    photo_logo = open(path_to_main_logo_jpg, 'rb')
    txt = 'Я подручный бот-тренер Healthy Employer\n\n' + 'Чем могу помочь?'
    await message.answer_photo(caption=txt, reply_markup=get_start_keyboard(), photo=photo_logo)


@dp.callback_query_handler(Text(startswith="start_state"))
async def callbacks_num_start(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":
        await call.message.delete()
        await start_menu.menu(call.message)
    elif action == "2":
        await call.message.delete()
        await languages.change_language(call.message)
    elif action == "3":
        await call.message.delete()
        await call.message.answer(text='В разработке')
    elif action == '4':
        await call.message.delete()
        await commands.process_help_command(call.message)


async def cmd_start(message: types.Message):
    await start_bot(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
