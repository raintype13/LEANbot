from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio

TOKEN = "7244871285:AAF2Ic11UKNS5VJTYBDl5oM0jgWGDE1eWNI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Welcome to LEAN support. If you have any questions about the app, feel free to ask them here, and our moderators will review it.")

@dp.message()
async def echo(message: types.Message):
    await message.answer("Your question is accepted. We will review your request soon.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
