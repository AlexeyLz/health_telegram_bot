from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.productivity as pfk
from bot_settings import dp
import bot_texts as bt
import red_button.productivity_types.introduction_types.mental_activity as bw
import red_button.productivity_types.introduction_types.physical_activity as pw
import red_button.productivity_types.introduction_types.sedentary_labor as sw


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Умственный труд", callback_data="state_1_1.1"),
               types.InlineKeyboardButton(text="Физический труд", callback_data="state_1_1.2"),
               types.InlineKeyboardButton(text="Малоподвижный труд", callback_data="state_1_1.3"),
               types.InlineKeyboardButton(text="Назад", callback_data="state_1_1.4"),
               # types.InlineKeyboardButton(text="Помощь", callback_data="state_1_1.6")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def start_gymnastics(call):
    # photo1 = open('resources/1.1.1.png', 'rb')
    print(2222)
    # await bot.send_photo(call.message.chat.id, photo1, caption='это крутой спорт', reply_markup=get_keyboard())
    await call.message.answer(bt.gymnastics_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="state_1_1"))
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
        await sw.start_sedentary_work(call)
    elif action == "4":
        await call.message.delete()
        await pfk.start_productivity(call)

    await call.answer()
