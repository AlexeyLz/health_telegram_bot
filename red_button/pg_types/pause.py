from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg as pfk
from bot_settings import bot, dp
import bot_texts as bt
import red_button.gymnastics_types.brain_work as bw
import red_button.gymnastics_types.physical_work as pw
import red_button.gymnastics_types.mixed_work as mw
import red_button.gymnastics_types.sedentary_work as sw
def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Умственный труд", callback_data="state_1_4.1"),
               types.InlineKeyboardButton(text="Малоподвижный труд", callback_data="state_1_4.2"),
               types.InlineKeyboardButton(text="Средний физический труд ", callback_data="state_1_4.3"),
               types.InlineKeyboardButton(text="Тяжелый физический труд", callback_data="state_1_4.4"),
               types.InlineKeyboardButton(text="Назад", callback_data="state_1_4.5"),
               #types.InlineKeyboardButton(text="Помощь", callback_data="state_1_1.6")
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
        await pw.start_physical_work(call)

    elif action == "3":

        await call.message.delete()
        await mw.start_mixed_work(call)

    elif action == "4":

        await call.message.delete()
        await sw.start_sedentary_work(call)
    elif action == "5":
        await call.message.delete()
        await pfk.start_pfk(call)

    await call.answer()
