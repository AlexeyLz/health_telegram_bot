import aiogram
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.utils import executor
import languages
from bot_settings import bot, dp, path_to_main_gif, connection, path_to_main_logo, path_to_main_logo_jpg
from red_button import start_menu
import bot_texts as bt


def get_training_keyboard():
    buttons = [types.InlineKeyboardButton(text="🔴", callback_data="training_state_1"),
               types.InlineKeyboardButton(text="🔵", callback_data="training_state_2"),
               types.InlineKeyboardButton(text="⬅️", callback_data="training_state_3"),
               ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def get_start_keyboard():
    buttons = [types.InlineKeyboardButton(text="💪 Упражнения 💪", callback_data="start_state_1"),
               types.InlineKeyboardButton(text="🌍 Языки 🌍", callback_data="start_state_2"),
               types.InlineKeyboardButton(text="⏰ Расписание ⏰", callback_data="start_state_3"),
               types.InlineKeyboardButton(text="ℹ️ Информация ℹ️", callback_data="start_state_4"),
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def save_user(user_id):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id =%s', (str(user_id),))
    entry = cursor.fetchone()
    if entry is None:
        cursor.execute('INSERT INTO users VALUES(' + str(user_id) + ',0,0)')
    connection.commit()
    cursor.close()


@dp.message_handler(commands="start")
async def console_start(message: types.Message):
    button_to_start = types.KeyboardButton(bt.back_to_start)
    to_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_to_start)
    me = await bot.get_me()
    name_bot = me.first_name
    txt = 'Привет, ' + str(message.from_user.first_name) + \
          '\nДобро пожаловать в ' + str(name_bot)
    await message.answer(text=txt, reply_markup=to_start_keyboard)
    print('Зарегался', message.from_user.id)

    await start_bot(message)
    save_user(message.from_user.id)


@dp.message_handler(commands="support")
async def support(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Написать в чат',
                                        url='https://t.me/healthyemployersupport')
    keyboard.add(button)
    text = 'Нужна помощь или заметили баг?\nНапиши в чат!'
    await message.answer(text, reply_markup=keyboard)


@dp.message_handler(commands="about")
async def about(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Our Site', url='https://healthyemployer.info/')
    keyboard.add(button)
    button = types.InlineKeyboardButton('Our Instagram',
                                        url='https://www.instagram.com/healthyemployer/')
    keyboard.add(button)
    button = types.InlineKeyboardButton('Our Telegram',
                                        url='https://t.me/HealthyEmployer')
    keyboard.add(button)
    text = '..::Healthy Employer::..\n\nНаш сайт\nhttps://healthyemployer.info/\n\nНаш ' \
           'Instagram\nhttps://www.instagram.com/healthyemployer/\n\nНаш Telegram\nhttps://t.me/HealthyEmployer'
    await message.answer(text, reply_markup=keyboard)


async def start_bot(message: types.Message):
    photo_logo = open(path_to_main_logo_jpg, 'rb')
    txt = 'Я подручный бот-тренер Healthy Employer\n\n'+'Чем могу помочь?'
    await message.answer_photo(caption=txt, reply_markup=get_start_keyboard(),photo=photo_logo)


async def start_training(message: types.Message):
    photo_gif = open(path_to_main_gif, 'rb')
    me = await bot.get_me()
    name_bot = me.first_name

    txt = 'Добро пожаловать в ' + str(name_bot) + bt.main_text
    await message.answer_animation(animation=photo_gif, reply_markup=get_training_keyboard(), caption=txt)


@dp.callback_query_handler(Text(startswith="start_state"))
async def callbacks_num_start(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":
        await call.message.delete()
        await start_training(call.message)
    elif action == "2":
        await call.message.delete()
        await languages.change_language(call.message)
    elif action == "3":
        await call.message.delete()
        await call.message.answer(text='В разработке')
    elif action == '4':
        await call.message.delete()
        await process_help_command(call.message)


@dp.callback_query_handler(Text(startswith="training_state"))
async def callbacks_num_training(call: types.CallbackQuery):
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
        await start_bot(call.message)


@dp.message_handler(Text(equals=bt.back_to_start))
async def back_to_start(message: types.Message):
    await start_bot(message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(bt.hello_text)


async def cmd_start(message: types.Message):
    await start_bot(message)

@dp.message_handler(commands=['donate'])
async def process_donate_command(message: types.Message):
    await message.answer('Для связи - @Oleksimus')


@dp.message_handler(commands=['off'])
async def process_off_command(message: types.Message):
    await message.answer('Команда находится в разработке.')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, bt.do_not_understand)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
