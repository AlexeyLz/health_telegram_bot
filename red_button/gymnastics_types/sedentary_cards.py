from aiogram.dispatcher.filters import Text
from aiogram import types
from bot_settings import connection
import red_button.gymnastics_types.sedentary_work as sw
from bot_settings import dp
from card import Card
import bot_texts as bt


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Далее", callback_data="sedentary_cards_state_1.1"),
               types.InlineKeyboardButton(text="Назад", callback_data="sedentary_cards_state_1.2"),

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


async def start_sedentary_cards(call):
    number_exercise = 1
    cursor = connection.cursor()
    change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)
    card = Card(number_exercise)

    await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(), reply_markup=get_keyboard())
    del card
    # except:
    #     await call.message.answer('Непредвиденная ошибка. /start - чтобы исправить')


@dp.callback_query_handler(Text(startswith="sedentary_cards_state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]

    cursor = connection.cursor()
    cursor.execute("SELECT sedentary_work_exercise_number FROM users WHERE user_id=%s", (call.from_user.id,))

    number_exercise = cursor.fetchone()
    print(11111111,number_exercise)
    number_exercise = number_exercise[0]
    cursor.execute("SELECT COUNT(*) from sedentary_work_table")
    table_size = list(cursor)[0][0]
    if action == "1":

        number_exercise += 1
        change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)
        print('number ex', number_exercise)
        await call.message.delete()
        if number_exercise <= table_size:
            card = Card(number_exercise)
            await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(),
                                            reply_markup=get_keyboard())
            del card
        else:
            await call.message.answer(text='конец трени. нужно доработать.')

    elif action == "2":

        await call.message.delete()

        if number_exercise <= 0:

            number_exercise = 0
            change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

            await sw.start_sedentary_work(call)
        else:
            number_exercise -= 1
            change_number_exercise_from_db(cursor, number_exercise, call.from_user.id)

            card = Card(number_exercise)

            await call.message.answer_photo(photo=card.get_image(), caption=card.get_description(),
                                            reply_markup=get_keyboard())
            del card

    await call.answer()
