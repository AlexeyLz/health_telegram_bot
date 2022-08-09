# from telebot import TeleBot
# from aiogram import types


from aiogram.dispatcher.filters import Text
from aiogram import types
from bot_settings import bot, dp
import red_button.pg as pfk
import red_button.pr as pr
import red_button.ppzv as ppzv
import red_button.ppfp as ppfp
import bot_texts as bt


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Производственная Гимнастика", callback_data="main_state_1"),
               types.InlineKeyboardButton(text="Послетрудовая реабилитация", callback_data="main_state_2"),
               types.InlineKeyboardButton(text="Профилактика профессиональных заболеваний",
                                          callback_data="main_state_3"),
               types.InlineKeyboardButton(text="Профессионально-прикладная изическая подготовка",
                                          callback_data="main_state_4")

               ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def menu(message: types.Message):
    txt = bt.chose_action

    await message.answer(txt, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="main_state"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":

        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()

        await pfk.start_pfk(call)
    elif action == "2":

        await call.message.delete()

        await pr.start_pr(call)
    elif action == "3":

        await call.message.edit_text('3')
        await ppzv.start_ppzv(call)
    elif action == "4":

        await call.message.edit_text('3')
        await ppfp.start_ppfp(call)
    await call.answer()
