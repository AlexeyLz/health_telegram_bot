from aiogram.dispatcher.filters import Text
from aiogram import types

import main
from bot_settings import bot, dp, path_to_main_gif, connection, path_to_main_logo


def get_languages_keyboard():
    buttons = [types.InlineKeyboardButton(text="🇷🇺 Русский 🇷🇺", callback_data="language_state_1"),
               types.InlineKeyboardButton(text="🇬🇧 English 🇬🇧", callback_data="language_state_2"),
               types.InlineKeyboardButton(text="🇪🇸 Español 🇪🇸", callback_data="language_state_3"),
               types.InlineKeyboardButton(text="Назад", callback_data="language_state_4"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def change_language(message):
    txt = 'Выберите язык'
    await message.answer(text=txt, reply_markup=get_languages_keyboard())


@dp.callback_query_handler(Text(startswith="language_state"))
async def callbacks_num_start(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":
        await call.message.delete()
        await call.message.answer(text='Данный язык уже выбран')

    elif action == "2":
        await call.message.delete()
        await call.message.answer(text='В разработке')
    elif action == "3":
        await call.message.delete()
        await call.message.answer(text='В разработке')
    elif action == '4':
        await call.message.delete()
        await main.start_bot(call.message)
