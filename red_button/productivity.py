from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.productivity_types.introduction as gymnastics
import red_button.productivity_types.pause as pause
import red_button.productivity_types.minute as minute
import red_button.productivity_types.micropause as micropause
from bot_settings import dp
import red_button.start_menu as sm
import bot_texts as bt


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Вводная часть", callback_data="pfk_state_1.1"),
               types.InlineKeyboardButton(text="Пауза", callback_data="pfk_state_1.2"),
               types.InlineKeyboardButton(text="Минута", callback_data="pfk_state_1.3"),
               types.InlineKeyboardButton(text="Микропауза", callback_data="pfk_state_1.4"),
               types.InlineKeyboardButton(text="Назад", callback_data="pfk_state_1.5")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_productivity(call):
    await call.message.answer(bt.p_gymnastics_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="pfk_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(123456)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await gymnastics.start_gymnastics(call)
    elif action == "2":

        await call.message.delete()
        await pause.start_pause(call)
    elif action == "3":

        await call.message.delete()
        await minute.start_minute(call)
    elif action == "4":

        await call.message.delete()
        await micropause.start_micropause(call)

    elif action == "5":
        await call.message.delete()
        await sm.menu(call.message)

    await call.answer()
