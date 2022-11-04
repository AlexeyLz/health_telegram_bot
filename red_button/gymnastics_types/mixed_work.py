from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg_types.gymnastics as gymnastics
from bot_settings import dp
import bot_texts as bt

STATE = 'mixed_work'


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data=STATE + "_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=STATE + "_state_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_mixed_work(call):
    await call.message.answer(bt.mixed_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith=STATE + "_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await call.message.answer('Данная ветка находится в разработке.')
    elif action == "2":

        await call.message.delete()
        await gymnastics.start_gymnastics(call)

    await call.answer()
