from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import bot_texts as bt
from bot_settings import bot, TOKEN, dp
import red_button.start_menu as sm



def get_keyboard1():
    buttons = [types.InlineKeyboardButton(text="Для занятых тяжелым физическим трудом", callback_data="state_2.1"),
               types.InlineKeyboardButton(text="Для занятых нервно-напряженным трудом", callback_data="state_2.2"),
               types.InlineKeyboardButton(text="Назад",
                                          callback_data="state_2.3")

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_pr(call):
    await call.message.answer(bt.pr_desc, reply_markup=get_keyboard1())


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
    elif action == "3":

        await call.message.delete()
        await sm.menu(call.message)



    await call.answer()