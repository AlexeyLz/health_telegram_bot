# from telebot import TeleBot
# from aiogram import types


from aiogram.dispatcher.filters import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import textwrap
from bot_settings import bot, TOKEN, dp
import pfk
import pr
import ppzv
import ppfp



def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Производственная Гимнастика", callback_data="main_state_1"),
               types.InlineKeyboardButton(text="Послетрудовая реабилитация", callback_data="main_state_2"),
               types.InlineKeyboardButton(text="Профилактика профессиональных заболеваний во внерабочее время", callback_data="main_state_3"),
               types.InlineKeyboardButton(text="Профессионально-прикладная \nфизическая подготовка", callback_data="main_state_4")

               ]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard





@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    button_to_start = types.KeyboardButton('Вернуться в начало')
    to_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button_to_start)
    photo = open('start_image.png', 'rb')
    await message.answer_photo(photo=photo, reply_markup=to_start_keyboard)
    await message.answer("Выберите пункт", reply_markup=get_keyboard())





@dp.callback_query_handler(Text(startswith="main_state"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split("_")[2]
    if action == "1":

        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()

        await pfk.start_pfk(call)
    elif action == "2":

        #await call.message.edit_text('2')
        # await call.message.answer('kek')
        await call.message.delete()

        await pr.start_pr(call)
    elif action == "3":

        await call.message.edit_text('3')
        await ppzv.start_ppzv(call)
    elif action == "4":

        await call.message.edit_text('3')
        await ppfp.start_ppfp(call)
    await call.answer()


@dp.message_handler(Text(equals="Вернуться в начало"))
async def with_puree(message: types.Message):
    await cmd_start(message)


@dp.message_handler(lambda message: message.text == "Я лох")
async def without_puree(message: types.Message):
    await message.reply("Да, ты лох!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Не понимаю тебя')
    # await msg.answer('Неизвестно, что ты хотел узнать...')


if __name__ == '__main__':
    executor.start_polling(dp)
