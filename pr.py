from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import gymnastics
from bot_settings import bot, TOKEN, dp




def get_keyboard1():
    buttons = [types.InlineKeyboardButton(text="Комплекс для людей, занятых тяжелым физическим трудом", callback_data="state_2.1"),
               types.InlineKeyboardButton(text="Комплекс для людей, занятых нервно-напряженным трудом", callback_data="state_2.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_pr(call):
    await call.message.answer("Выберите пункт", reply_markup=get_keyboard1())


@dp.callback_query_handler(Text(startswith="state_2"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        #await call.message.delete()
        await call.message.edit_text('физич')
    elif action == "2":

        await call.message.edit_text('нервно-напр')
        # await call.message.answer('kek')


    await call.answer()