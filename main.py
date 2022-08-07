from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.utils import executor
from bot_settings import bot, dp, path_to_main_gif
from red_button import start_menu
import bot_texts as bt


def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="🔴", callback_data="start_state_1"),
               types.InlineKeyboardButton(text="🔵", callback_data="start_state_2"),

               ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    button_to_start = types.KeyboardButton(bt.back_to_start)
    to_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_to_start)
    photo = open(path_to_main_gif, 'rb')
    me = await bot.get_me()
    name_bot = me.first_name
    txt = 'Привет, ' + str(message.from_user.first_name) + \
          '\nДобро пожаловать в ' + str(name_bot) + bt.main_text
    await message.answer_animation(animation=photo, reply_markup=to_start_keyboard)
    await message.answer(txt, reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="start_state"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":

        await call.message.delete()

        await start_menu.menu(call.message)
    elif action == "2":

        await call.message.delete()

        print(2)


@dp.message_handler(Text(equals=bt.back_to_start))
async def with_puree(message: types.Message):
    await cmd_start(message)





@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, bt.do_not_understand)


if __name__ == '__main__':
    executor.start_polling(dp)
