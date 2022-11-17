from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.productivity as pfk
from bot_settings import bot, dp
import bot_texts as bt
import red_button.pause_types.brain_work as bw
import red_button.pause_types.sedentary_labor as sl
import red_button.pause_types.hard_physical_labor as hpl


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Умственный труд", callback_data="state_1_4.1"),
               types.InlineKeyboardButton(text="Физический труд", callback_data="state_1_4.3"),#ТЯжелый физ труд
               types.InlineKeyboardButton(text="Малоподвижный труд", callback_data="state_1_4.2"),
               types.InlineKeyboardButton(text="Назад", callback_data="state_1_4.4"),
               # types.InlineKeyboardButton(text="Помощь", callback_data="state_1_1.5")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def start_pause(call):
    # photo1 = open('resources/1.1.1.png', 'rb')

    # await bot.send_photo(call.message.chat.id, photo1, caption='это крутой спорт', reply_markup=get_keyboard())
    await call.message.answer(bt.pause_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="state_1_4"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        await call.message.delete()
        await bw.start_brainwork(call)
        # with open('resources//1.1.1.txt', 'r', encoding='utf-8') as file:
        #     text = file.readline()
        # await call.message.delete()
        #
        # photo = open('resources/1.1.1.png', 'rb')
        #
        # await bot.send_photo(call.message.chat.id, photo, caption=text)
    elif action == "2":

        await call.message.delete()
        await sl.start_sedentary_labor(call)


    elif action == "3":

        await call.message.delete()
        await hpl.start_hard_physical_labor(call)
    elif action == "4":
        await call.message.delete()
        await pfk.start_productivity(call)

    await call.answer()
