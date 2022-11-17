from aiogram.dispatcher.filters import Text
from aiogram import types

import bot_texts
import main
from bot_settings import connection
import red_button.recovery_types.nervous_activity as ften
from bot_settings import dp
from card import Card

import bot_texts as bt
TABLE_NAME = 'recovery_nervous_activity'
USUAL_STATE = 'recovery_nervous_activity_cards'
END_STATE = 'recovery_nervous_activity_cards_end'

def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Далее", callback_data=USUAL_STATE+"_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data=USUAL_STATE+"_state_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def get_end_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Разумеется", callback_data=END_STATE+"_state_1.1"),
        types.InlineKeyboardButton(text="Назад", callback_data=END_STATE+"_state_1.2"),

        ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def change_number_exercise_from_db(cursor, number_exercise, user_id):
    cursor.execute(
        "UPDATE users SET exercise_number = %s WHERE user_id = %s", (str(number_exercise), str(
            user_id)))
    connection.commit()
    cursor.close()


async def start_ftenc_cards(call):
    number_exercise = 1
    cursor = connection.cursor()
    change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)
    card = Card(number_exercise, TABLE_NAME)

    await call.message.answer_video(video=card.get_video(), caption=card.get_description(), reply_markup=get_keyboard())
    del card
    print('hi')
    # except:
    #     await call.message.answer('Непредвиденная ошибка. /start - чтобы исправить')


@dp.callback_query_handler(Text(startswith=END_STATE+"_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]

    if action == '1':
        await call.message.delete()
        await main.cmd_start(call.message)
    elif action == '2':
        await call.message.delete()
        cursor = connection.cursor()
        cursor.execute("SELECT exercise_number FROM users WHERE user_id=%s", (call.from_user.id,))

        number_exercise = cursor.fetchone()

        number_exercise = number_exercise[0]
        number_exercise -= 1
        change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

        card = Card(number_exercise, TABLE_NAME)

        await call.message.answer_video(video=card.get_video(), caption=card.get_description(),
                                        reply_markup=get_keyboard())
        del card


@dp.callback_query_handler(Text(startswith=USUAL_STATE+"_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    print('dsgi')
    cursor = connection.cursor()
    cursor.execute("SELECT exercise_number FROM users WHERE user_id=%s", (call.from_user.id,))

    number_exercise = cursor.fetchone()

    number_exercise = number_exercise[0]
    cursor.execute("SELECT COUNT(*) from " + TABLE_NAME)
    table_size = list(cursor)[0][0]
    if action == "1":

        number_exercise += 1
        change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

        await call.message.delete()
        if number_exercise <= table_size:
            card = Card(number_exercise, TABLE_NAME)
            await call.message.answer_video(video=card.get_video(), caption=card.get_description(),
                                            reply_markup=get_keyboard())
            del card
        else:

            await call.message.answer(text=bot_texts.sedentary_end, reply_markup=get_end_keyboard())

    elif action == "2":

        await call.message.delete()

        if number_exercise <= 1:

            number_exercise = 0
            change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

            await ften.start_ften(call)
        else:
            number_exercise -= 1
            change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

            card = Card(number_exercise, TABLE_NAME)

            await call.message.answer_video(video=card.get_video(), caption=card.get_description(),
                                            reply_markup=get_keyboard())
            del card

    await call.answer()
