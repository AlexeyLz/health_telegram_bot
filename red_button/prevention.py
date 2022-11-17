from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import bot_texts as bt
from bot_settings import bot, TOKEN, dp
import red_button.start_menu as sm
import red_button.prevention_types.breathing_exercises as be
import red_button.prevention_types.prevention_of_osteochondrosis as po
import red_button.prevention_types.with_increased_neuro_emotional_stress as win
import red_button.prevention_types.flat_feet_and_varicose_veins as ffv
import red_button.prevention_types.strengthening_the_arch_of_the_foot_with_flat_feet as sta
import red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases as prev_of_j


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Дыхательные упражнения", callback_data="state_3.1"),
               types.InlineKeyboardButton(text="Профилактика Остеохондроза", callback_data="state_3.2"),
               types.InlineKeyboardButton(text="При выполнении нервно-эмоциональном напряжении",
                                          callback_data="state_3.3"),
               types.InlineKeyboardButton(text="При плоскостопии и варикозном рассширении вен",
                                          callback_data="state_3.4"),
               types.InlineKeyboardButton(text="Упраженения укрепляющие свод стопы при плоскостопии",
                                          callback_data="state_3.5"),
               types.InlineKeyboardButton(text="Для профилактики заболеваний суставов",
                                          callback_data="state_3.6"),
               types.InlineKeyboardButton(text="Назад",
                                          callback_data="state_3.7"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_prevention(call):
    await call.message.answer(bt.ppzv_desc, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="state_3"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await be.start_be(call)
    elif action == "2":

        await call.message.delete()
        await po.start_po(call)
    elif action == "3":

        await call.message.delete()
        await win.start_win(call)
    elif action == "4":
        await call.message.delete()
        await ffv.start_ffv(call)
    elif action == "5":

        await call.message.delete()
        await sta.start_sta(call)
        # await call.message.answer('kek')
    elif action == "6":

        await call.message.delete()
        await prev_of_j.start_prevention_of_joint(call)
    elif action == "7":

        await call.message.delete()
        await sm.menu(call.message)

    await call.answer()
