from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6859939400:AAFeizQ3YrvecO5BAK8MIpHWAantRY8yxo0')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(
        url='https://iskrapower.github.io/project')))
    await message.answer('Привет, мой друг!', reply_markup=markup)


executor.start_polling(dp)

