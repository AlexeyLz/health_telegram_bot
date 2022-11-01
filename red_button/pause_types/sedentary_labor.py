from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg_types.pause as pause
from bot_settings import dp
import bot_texts as bt
import red_button.pause_types.brain_work_cards as bwc

def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Начать", callback_data="sedentary_labor_state1_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data="sedentary_labor_state1_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_sedentary_labor(call):
    await call.message.answer(bt.brain_work_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="sedentary_labor_state1_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(12222)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()

        await bwc.start_brainwork_cards(call)
    elif action == "2":


        await call.message.delete()
        await pause.start_pause(call)


    await call.answer()