from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg_types.gymnastics as gymnastics
from bot_settings import dp
import bot_texts as bt


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data="brain_work_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data="brain_work_state_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_brainwork(call):
    await call.message.answer(bt.brain_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="brain_work_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await call.message.answer('Ветка пока не закончена')
    elif action == "2":


        await call.message.delete()
        await gymnastics.start_gymnastics(call)


    await call.answer()