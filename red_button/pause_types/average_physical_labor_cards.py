from aiogram.dispatcher.filters import Text
from aiogram import types

import bot_texts
from bot_settings import connection
import red_button.pause_types.average_physical_labor as apl
from bot_settings import dp
from card import Card

import bot_texts as bt
table_name = 'working_standing_with_average_physical_activity'

def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Далее", callback_data="average_physical_labor_cards_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data="average_physical_labor_cards_state_1.2"),

               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def get_end_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Разумеется", callback_data="average_physical_labor_cards_end_state_1.1"),
        types.InlineKeyboardButton(text="Назад", callback_data="average_physical_labor_cards_end_state_1.2"),

        ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def change_number_exercise_from_db(cursor, number_exercise, user_id):
    cursor.execute(
        "UPDATE users SET sedentary_work_exercise_number = %s WHERE user_id = %s", (str(number_exercise), str(
            user_id)))
    connection.commit()
    cursor.close()


async def start_apl_cards(call):
    number_exercise = 1
    cursor = connection.cursor()
    change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)
    card = Card(number_exercise, table_name)

    await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(), reply_markup=get_keyboard())
    del card
    print('hi')
    # except:
    #     await call.message.answer('Непредвиденная ошибка. /start - чтобы исправить')


@dp.callback_query_handler(Text(startswith="average_physical_labor_cards_end_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]

    if action == '1':
        await call.message.delete()
        await apl.start_apl(call)
    elif action == '2':
        await call.message.delete()
        cursor = connection.cursor()
        cursor.execute("SELECT sedentary_work_exercise_number FROM users WHERE user_id=%s", (call.from_user.id,))

        number_exercise = cursor.fetchone()

        number_exercise = number_exercise[0]
        number_exercise -= 1
        change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

        card = Card(number_exercise, table_name)

        await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(),
                                        reply_markup=get_keyboard())
        del card


@dp.callback_query_handler(Text(startswith="average_physical_labor_cards_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    print('dsgi')
    cursor = connection.cursor()
    cursor.execute("SELECT sedentary_work_exercise_number FROM users WHERE user_id=%s", (call.from_user.id,))

    number_exercise = cursor.fetchone()

    number_exercise = number_exercise[0]
    cursor.execute("SELECT COUNT(*) from " + table_name)
    table_size = list(cursor)[0][0]
    if action == "1":

        number_exercise += 1
        change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

        await call.message.delete()
        if number_exercise <= table_size:
            card = Card(number_exercise, table_name)
            await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(),
                                            reply_markup=get_keyboard())
            del card
        else:

            await call.message.answer(text=bot_texts.sedentary_end, reply_markup=get_end_keyboard())

    elif action == "2":

        await call.message.delete()

        if number_exercise <= 1:

            number_exercise = 0
            change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

            await apl.start_apl(call)
        else:
            number_exercise -= 1
            change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

            card = Card(number_exercise, table_name)

            await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(),
                                            reply_markup=get_keyboard())
            del card

    await call.answer()
