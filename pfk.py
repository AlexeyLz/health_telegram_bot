from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import gymnastics
from bot_settings import bot, TOKEN, dp




def get_keyboard1():
    buttons = [types.InlineKeyboardButton(text="Вводная гимнастика", callback_data="state_1.1"),
               types.InlineKeyboardButton(text="Физкультурная пауза", callback_data="state_1.2"),
               types.InlineKeyboardButton(text="Физкультурная минутка", callback_data="state_1.3"),
               types.InlineKeyboardButton(text="Микропауза активного отдыха", callback_data="state_1.4")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_pfk(call):
    await call.message.answer("Выберите пункт", reply_markup=get_keyboard1())


@dp.callback_query_handler(Text(startswith="state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await gymnastics.start_gymnastics(call)
    elif action == "2":

        await call.message.edit_text('2')
        # await call.message.answer('kek')
    elif action == "3":

        await call.message.edit_text('3')
    elif action == "3":

        await call.message.edit_text('3')

    await call.answer()