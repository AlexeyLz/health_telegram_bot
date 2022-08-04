# from telebot import TeleBot
# from aiogram import types


from aiogram.dispatcher.filters import Text
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import gymnastics
from bot_settings import bot, TOKEN, dp




def get_keyboard():
    buttons = [types.InlineKeyboardButton(text="Вводная гимнастика", callback_data="state_1.1"),
               types.InlineKeyboardButton(text="Физкультурная пауза", callback_data="state_1.2"),
               types.InlineKeyboardButton(text="Физкультурная минутка", callback_data="state_1.3"),
               types.InlineKeyboardButton(text="Микропауза активного отдыха", callback_data="state_1.4")
               ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard





@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Выберите пункт", reply_markup=get_keyboard())


@dp.callback_query_handler(Text(startswith="state_1"))
async def callbacks_num(call: types.CallbackQuery):
    action = call.data.split(".")[1]
    if action == "1":
        print(1)
        # await call.message.edit_text('Вы выбрали вводную гимнастику')
        await call.message.delete()
        await gymnastics.start_gymnastics(call)
    elif action == "2":

        await call.message.edit_text('2')
        # await call.message.answer('kek')
    elif action == "3":

        await call.message.edit_text('3')
    elif action == "3":

        await call.message.edit_text('3')

    await call.answer()


@dp.message_handler(Text(equals="Ты лох"))
async def with_puree(message: types.Message):
    await message.reply("Сам ты лох!")


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
