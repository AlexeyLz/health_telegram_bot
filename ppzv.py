from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import gymnastics
from bot_settings import bot, TOKEN, dp




def get_keyboard1():
    buttons = [types.InlineKeyboardButton(text="1 Дыхательные упражнения", callback_data="state_3.1"),
               types.InlineKeyboardButton(text="2 Профилактика Остеохондроза", callback_data="state_3.2"),
               types.InlineKeyboardButton(text="3 При выполнении нервно-эмоциональном напряжении",
                                          callback_data="state_3.3"),
               types.InlineKeyboardButton(text="4 При плоскостопии и варикозном рассширении вен",
                                          callback_data="state_3.4"),
               types.InlineKeyboardButton(text="5 Упраженения укрепляющие свод стопы при плоскостопии",
                                          callback_data="state_3.5"),
               types.InlineKeyboardButton(text="6 Для профилактики заболеваний суставов",
                                          callback_data="state_3.6"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard






async def start_ppzv(call):
    await call.message.answer("Выберите пункт", reply_markup=get_keyboard1())


@dp.callback_query_handler(Text(startswith="state_3"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        #await call.message.delete()
        await call.message.edit_text('1')
    elif action == "2":

        await call.message.edit_text('нервно-напр2')
        # await call.message.answer('kek')
    elif action == "3":

        await call.message.edit_text('нервно-напр3')
    elif action == "4":

        await call.message.edit_text('нервно-напр4')
    elif action == "5":

        await call.message.edit_text('нервно-напр5')
        # await call.message.answer('kek')
    elif action == "6":

        await call.message.edit_text('нервно-напр6')




    await call.answer()