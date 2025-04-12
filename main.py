import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command

bot = Bot( token='7753299696:AAGUKFyMKdk_J9EuDNxfE544kbhqV6GiS1I')

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Open', web_app=WebAppInfo(url='https://gor12534.github.io/websitefortg/'))]
        ],
        resize_keyboard=True
    )
    await message.answer("Hello 👋", reply_markup=markup)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
