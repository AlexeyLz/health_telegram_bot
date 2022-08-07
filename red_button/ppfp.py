from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import bot_texts as bt
from bot_settings import bot, TOKEN, dp
import red_button.start_menu as sm



def get_keyboard1():
    buttons = [types.InlineKeyboardButton(text="Тренировки дома", callback_data="state_4.1"),
               types.InlineKeyboardButton(text="Тренировки на улице", callback_data="state_4.2"),
               types.InlineKeyboardButton(text="Тренировке в тренажерном зале", callback_data="state_4.3"),
               types.InlineKeyboardButton(text="Назад", callback_data="state_4.4")


               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_ppfp(call):
    await call.message.answer("Выберите пункт", reply_markup=get_keyboard1())


@dp.callback_query_handler(Text(startswith="state_4"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        # await call.message.delete()
        # await gymnastics.start_gymnastics(call)
        await call.message.edit_text('just1')

    elif action == "2":

        await call.message.edit_text('just2')
        # await call.message.answer('kek')
    elif action == "3":

        await call.message.edit_text('just3')
    elif action == "3":

        await call.message.edit_text('just4')
    elif action == "4":

        await call.message.delete()
        await sm.menu(call.message)


    await call.answer()