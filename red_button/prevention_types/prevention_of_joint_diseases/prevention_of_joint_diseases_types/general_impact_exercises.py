from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases as prev_of_j
from bot_settings import dp
import bot_texts as bt
import \
    red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases_types.general_impact_exercises_cards as gic

STATE = 'prevention_of_joint_diseases_part_4'


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data=STATE + "_state1_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=STATE + "_state1_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_gi(call):
    await call.message.answer(bt.brain_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith=STATE + "_state1_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()

        await gic.start_gic_cards(call)
    elif action == "2":

        await call.message.delete()
        await prev_of_j.start_prevention_of_joint(call)

    await call.answer()
