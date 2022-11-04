from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg_types.minute as minute
from bot_settings import dp
import bot_texts as bt
import red_button.minute_types.relax_back_muscles_and_improve_posture_cards as rbmc

STATE = 'relax_back_muscles_and_improve_posture'


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data=STATE + "_state1_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=STATE + "_state1_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_rbm(call):
    await call.message.answer(bt.brain_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith=STATE + "_state1_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()

        await rbmc.start_rbmc_cards(call)
    elif action == "2":

        await call.message.delete()
        await minute.start_minute(call)

    await call.answer()
