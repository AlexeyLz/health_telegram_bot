import aiogram
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.utils import executor
from aiogram.utils.markdown import link

from bot_settings import bot, dp, path_to_main_gif, connection, path_to_main_logo
from red_button import start_menu
import bot_texts as bt


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="🔴", callback_data="start_state_1"),
               types.InlineKeyboardButton(text="🔵", callback_data="start_state_2"),
               types.InlineKeyboardButton(text="❔", callback_data="start_state_3"),
               ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def save_user(user_id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id =%s', (str(user_id),))
    entry = cursor.fetchone()

    if entry is None:
        cursor.execute('INSERT INTO users VALUES(' + str(user_id) + ',0)')

    connection.commit()
    cursor.close()


@dp.message_handler(commands="start")
async def console_start(message: types.Message):
    await cmd_start(message)
    print(message.from_user.id)
    save_user(message.from_user.id)


@dp.message_handler(commands="back_to_start")
async def cmd_start(message: types.Message):
    button_to_start = types.KeyboardButton(bt.back_to_start)
    to_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_to_start)
    photo_gif = open(path_to_main_gif, 'rb')
    photo_logo = open(path_to_main_logo, 'rb')
    me = await bot.get_me()
    name_bot = me.first_name
    txt = 'Привет, ' + str(message.from_user.first_name) + \
          '\nДобро пожаловать в ' + str(name_bot) + bt.main_text
    await message.answer(text='🏁    🏁   🏁   🏁   🏁', reply_markup=to_start_keyboard)
    await message.answer_animation(animation=photo_gif, reply_markup=get_keyboard(), caption=txt)

    # await message.answer('', reply_markup=)


@dp.callback_query_handler(Text(startswith="start_state"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[2]

    if action == "1":

        await call.message.delete()

        await start_menu.menu(call.message)
    elif action == "2":

        await call.message.delete()
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('HealthyEmployer.exe', url='https://files.fm/u/3qyjtrqnu')
        keyboard.add(button)

        await call.message.answer('🔗 Ссылка на скачивание программы', reply_markup=keyboard)

    elif action == "3":

        await call.message.delete()

        await process_help_command(call.message)


@dp.message_handler(Text(equals=bt.back_to_start))
async def with_puree(message: types.Message):
    await cmd_start(message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(bt.hello_text)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, bt.do_not_understand)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
