from aiogram.dispatcher.filters import Text
from aiogram import types

import red_button.pg as pfk
from bot_settings import bot, dp
import bot_texts as bt
import red_button.minute_types.general_impact as gi
import red_button.minute_types.reduce_eye_fatigue as ref
import red_button.minute_types.removing_fatigue_from_the_shoulder_girdle_and_arms as rem_fatig
import red_button.minute_types.relieve_fatigue_from_the_muscles_of_the_hand as rff
import red_button.minute_types.relax_back_muscles_and_improve_posture as rbm
import red_button.minute_types.rest_leg_muscles as rlm
import red_button.minute_types.relieve_fatigue_from_the_lower_back_and_back as rfb
import red_button.minute_types.increase_blood_circulation_in_the_legs_and_pelvis as ibc
import red_button.minute_types.rest_of_the_neck_muscles as ron


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Общее воздействие", callback_data="state_1_3.1"),
               types.InlineKeyboardButton(text="Снижение утомления глаз", callback_data="state_1_3.2"),
               types.InlineKeyboardButton(text="Отдых мышц шеи", callback_data="state_1_3.3"),
               types.InlineKeyboardButton(text="Снятие утомления с плечевого пояса и рук", callback_data="state_1_3.4"),
               types.InlineKeyboardButton(text="Снятие утомления с мышц кисти", callback_data="state_1_3.5"),
               types.InlineKeyboardButton(text="Отдых мышц спины и улучшения осанки", callback_data="state_1_3.6"),
               types.InlineKeyboardButton(text="Снятие усталости с поясницы и спины", callback_data="state_1_3.7"),
               types.InlineKeyboardButton(text="Усиление кровообращения ног и таза", callback_data="state_1_3.8"),
               types.InlineKeyboardButton(text="Отдых мышц ног", callback_data="state_1_3.9"),
               types.InlineKeyboardButton(text="Назад", callback_data="state_1_3.10"),
               # types.InlineKeyboardButton(text="Помощь", callback_data="state_1_1.6")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


async def start_minute(call):
    # photo1 = open('resources/1.1.1.png', 'rb')

    # await bot.send_photo(call.message.chat.id, photo1, caption='это крутой спорт', reply_markup=get_keyboard())
    await call.message.answer(bt.minute_desc, reply_markup=get_keyboard())
    print('kekkk')


@dp.callback_query_handler(Text(startswith="state_1_3"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        await call.message.delete()
        await gi.start_gic(call)

    elif action == "2":

        await call.message.delete()
        await ref.start_refc(call)

    elif action == "3":

        await call.message.delete()
        await ron.start_ron(call)

    elif action == "4":

        await call.message.delete()
        await rem_fatig.start_rem_fatig(call)
    elif action == "5":

        await call.message.delete()
        await rff.start_rff(call)
    elif action == "6":

        await call.message.delete()
        await rbm.start_rbm(call)
    elif action == "7":

        await call.message.delete()
        await rfb.start_rffb(call)
    elif action == "8":

        await call.message.delete()
        await ibc.start_ibc(call)
    elif action == "9":

        await call.message.delete()
        await rlm.start_rlm_fatig(call)
    elif action == "10":
        await call.message.delete()
        await pfk.start_pfk(call)

    await call.answer()
