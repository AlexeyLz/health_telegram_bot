from aiogram.dispatcher.filters import Text
from aiogram import Bot, types

import bot_texts as bt
from bot_settings import bot, TOKEN, dp

import red_button.prevention as ppzv
import red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases_types.exercises_for_arms_and_shoulder_girdle as ef
import red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases_types.general_impact_exercises as gi
import red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases_types.exercises_for_the_muscles_of_the_feet_and_pelvis as efm
import red_button.prevention_types.prevention_of_joint_diseases.prevention_of_joint_diseases_types.exercises_for_the_torso as eft
def get_keyboard1():
    buttons = [types.InlineKeyboardButton(text="Упражнения для рук и плечевого пояса", callback_data="state_prev3.1"),
               types.InlineKeyboardButton(text="Упражнения для  мышц ступней ног и области таза",
                                          callback_data="state_prev3.2"),
               types.InlineKeyboardButton(text="Упражнения для туловища",
                                          callback_data="state_prev3.3"),
               types.InlineKeyboardButton(text="Упражнения общего воздействия",
                                          callback_data="state_prev3.4"),
               types.InlineKeyboardButton(text="Назад",
                                          callback_data="state_prev3.5"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_prevention_of_joint(call):
    await call.message.answer("👇Выберите последнюю дверь 👇", reply_markup=get_keyboard1())


@dp.callback_query_handler(Text(startswith="state_prev3"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await ef.start_ef(call)
    elif action == "2":
        await call.message.delete()
        await efm.start_efm(call)
    elif action == "3":
        await call.message.delete()
        await eft.start_eft(call)
    elif action == "4":
        await call.message.delete()
        await gi.start_gi(call)
    elif action == "5":
        await call.message.delete()
        await ppzv.start_prevention(call)
