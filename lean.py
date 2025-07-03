from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

TOKEN = "8184541285:AAGcPC0houytdSbaNgg5eoKfbC9vu5DDMbw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    # Задаём путь к картинке как переменную
    photo_path = r"\BOTimage.png"
    photo = FSInputFile(photo_path)
    
    text = (
        "Welcome to LEAN App!\n\n"
        "This application allows you to farm $LEAN points by playing the game. "
        "Later, you will be able to earn real money through airdrops based on your points. "
        "Use the buttons below to start the app, join our community channel, or contact support."
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                
                InlineKeyboardButton(
                    text="Join Channel",
                    url="https://t.me/LEAN_cups"
                ),
                InlineKeyboardButton(
                    text="Support",
                    url="https://t.me/LEANcup_Supportbot"
                )
            ]
        ]
    )

    await message.answer_photo(photo=photo, caption=text, reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
