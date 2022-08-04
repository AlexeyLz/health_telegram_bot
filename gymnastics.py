from aiogram.dispatcher.filters import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from bot_settings import bot, TOKEN, dp


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Умственный труд", callback_data="state_1_1.1"),
               types.InlineKeyboardButton(text="Физический труд", callback_data="state_1_1.2"),
               types.InlineKeyboardButton(text="Смешанный труд", callback_data="state_1_1.3"),
               types.InlineKeyboardButton(text="Малоподвижный труд", callback_data="state_1_1.4")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def start_gymnastics(call):
    await call.message.answer('Выберите пункт', reply_markup=get_keyboard())


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

    await call.answer()
