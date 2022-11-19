import aiogram
from aiogram.dispatcher.filters import Text
from aiogram import types
from bot_settings import bot, dp, path_to_main_gif, connection, path_to_main_logo, path_to_main_logo_jpg, TOKEN
from red_button import start_menu
import bot_texts as bt
from main import start_bot, save_user


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


@dp.message_handler(commands=['donate'])
async def process_donate_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Поддержать',
                                        url='https://www.patreon.com/healthyemployer')
    keyboard.add(button)
    text = 'Поддержать нас подпиской - https://www.patreon.com/healthyemployer'
    await message.answer(text, reply_markup=keyboard)


@dp.message_handler(commands=['off'])
async def process_off_command(message: types.Message):
    await message.answer('Команда находится в разработке.')


@dp.message_handler(commands=['users'])
async def get_users(message: types.Message):
    print('admin command')
    try:

        arguments = message.get_args()
        print(arguments)
        if str(arguments) == str(TOKEN[TOKEN.index(':') + 1:]):
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            text = str(len(users)) + '\n'
            for user in users:
                text += '[id] - ' + str(user[0]) + ' |||  [ex_num] - ' + str(user[2]) + '\n'
            await bot.send_message(message.from_user.id, text)
            return
        await bot.send_message(message.from_user.id, bt.do_not_understand)
    except:
        await bot.send_message(message.from_user.id, bt.do_not_understand)


@dp.message_handler(Text(equals=bt.back_to_start))
async def back_to_start(message: types.Message):
    await start_bot(message)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(bt.hello_text)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, bt.do_not_understand)
