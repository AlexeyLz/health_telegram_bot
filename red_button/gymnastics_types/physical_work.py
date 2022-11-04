from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg_types.gymnastics as gymnastics
import red_button.gymnastics_types.physical_work_cards as pwc
from bot_settings import dp
import bot_texts as bt

STATE = 'physical_labor'


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data=STATE + "_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=STATE + "_state_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_physical_work(call):
    await call.message.answer(bt.physical_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith=STATE + "_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await pwc.start_physical_work_cards(call)
    elif action == "2":

        await call.message.delete()
        await gymnastics.start_gymnastics(call)

    await call.answer()
