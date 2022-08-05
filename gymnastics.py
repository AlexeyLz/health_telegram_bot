from aiogram.dispatcher.filters import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import pfk
from bot_settings import bot, TOKEN, dp


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Умственный труд", callback_data="state_1_1.1"),
               types.InlineKeyboardButton(text="Физический труд", callback_data="state_1_1.2"),
               types.InlineKeyboardButton(text="Смешанный труд", callback_data="state_1_1.3"),
               types.InlineKeyboardButton(text="Малоподвижный труд", callback_data="state_1_1.4"),
               types.InlineKeyboardButton(text="Назад", callback_data="state_1_1.5"),
               types.InlineKeyboardButton(text="Помощь", callback_data="state_1_1.6")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def start_gymnastics(call):
    photo1 = open('test.png', 'rb')
    #await call.message.answer('Выберите пункт228', reply_markup=get_keyboard())
    await bot.send_photo(call.message.chat.id, photo1, caption='это крутой спорт',reply_markup=get_keyboard())

@dp.callback_query_handler(Text(startswith="state_1_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        with open('1.1.1.txt', 'r', encoding='utf-8') as file:
            text = file.readline()
        await call.message.delete()

        photo = open('1.1.1.png', 'rb')

        await bot.send_photo(call.message.chat.id, photo, caption=text)



    elif action == "2":

        await call.message.edit_text('2')

    elif action == "3":

        await call.message.edit_text('3.1')
    elif action == "3":

        await call.message.edit_text('3.1')
    elif action == "4":

        await call.message.edit_text('3.1')
    elif action == "5":
        print(5)
        await pfk.start_pfk(call)

    await call.answer()
