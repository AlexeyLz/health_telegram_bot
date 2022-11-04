from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg_types.micropause as micropause
import red_button.micropause_types.increasing_excitability_of_the_nervous_system_cards as iec
from bot_settings import dp
import bot_texts as bt

STATE = 'increasing_excitability_of_the_nervous_system'


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data=STATE + "_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=STATE + "_state_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_ie(call):
    await call.message.answer(bt.physical_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith= STATE+"_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await iec.start_iec(call)

    elif action == "2":

        await call.message.delete()
        await micropause.start_micropause(call)

    await call.answer()
