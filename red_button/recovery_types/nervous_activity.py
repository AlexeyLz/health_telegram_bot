from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.recovery as pr
from bot_settings import dp
import bot_texts as bt
import red_button.recovery_types.nervous_activity_cards as ftenc

STATE = 'recovery_nervous_activity'


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data=STATE + "_state1_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=STATE + "_state1_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_ften(call):
    await call.message.answer(bt.brain_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith=STATE + "_state1_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()

        await ftenc.start_ftenc_cards(call)
    elif action == "2":

        await call.message.delete()
        await pr.start_recovery(call)

    await call.answer()
