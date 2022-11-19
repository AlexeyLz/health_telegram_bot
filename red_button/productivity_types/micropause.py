from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.productivity as pfk
from bot_settings import dp
import bot_texts as bt
import red_button.productivity_types.micropause_types.eyes as ef
import red_button.productivity_types.micropause_types.brain as ic
import red_button.productivity_types.micropause_types.decrease_of_the_CNS_tension as rt
import red_button.productivity_types.micropause_types.increase_of_the_CNS_tension as ie


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Глаза", callback_data="state_1_2.1"),#При утомлении глаз
               types.InlineKeyboardButton(text="Мозг", callback_data="state_1_2.2"),#Улучшающая мозговое кровообращение
               types.InlineKeyboardButton(text="Снижение напряжения нервной системы", callback_data="state_1_2.3"),
               types.InlineKeyboardButton(text="Повышение напряжения нервной системы", callback_data="state_1_2.4"),#Повышающая возбудимость нервной системы"
               types.InlineKeyboardButton(text="Назад", callback_data="state_1_2.5"),
               # types.InlineKeyboardButton(text="Помощь", callback_data="state_1_1.6")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def start_micropause(call):
    # photo1 = open('resources/1.1.1.png', 'rb')

    # await bot.send_photo(call.message.chat.id, photo1, caption='это крутой спорт', reply_markup=get_keyboard())
    await call.message.answer(bt.micropause_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="state_1_2"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        await call.message.delete()
        await ef.start_ef(call)
        # with open('resources//1.1.1.txt', 'r', encoding='utf-8') as file:
        #     text = file.readline()
        # await call.message.delete()
        #
        # photo = open('resources/1.1.1.png', 'rb')
        #
        # await bot.send_photo(call.message.chat.id, photo, caption=text)




    elif action == "2":

        await call.message.delete()
        #await ic.start_ic(call)
        await call.message.answer("В разработке.")

    elif action == "3":

        await call.message.delete()
        await rt.start_rt(call)

    elif action == "4":

        await call.message.delete()
        await ie.start_ie(call)
    elif action == "5":
        await call.message.delete()
        await pfk.start_productivity(call)

    await call.answer()
