import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

# ----------- Первый бот: LEAN App -----------
TOKEN1 = "8184541285:AAGcPC0houytdSbaNgg5eoKfbC9vu5DDMbw"
bot1 = Bot(token=TOKEN1)
dp1 = Dispatcher()

@dp1.message(CommandStart())
async def send_welcome_lean(message: types.Message):
    photo_path = "BOTimage.png"  # путь к картинке должен быть относительным на сервере
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


# ----------- Второй бот: LEAN Support -----------
TOKEN2 = "7244871285:AAF2Ic11UKNS5VJTYBDl5oM0jgWGDE1eWNI"
bot2 = Bot(token=TOKEN2)
dp2 = Dispatcher()

@dp2.message(CommandStart())
async def send_welcome_support(message: types.Message):
    await message.answer(
        "Welcome to LEAN support. If you have any questions about the app, feel free to ask them here, and our moderators will review it."
    )

@dp2.message()
async def echo_support(message: types.Message):
    await message.answer("Your question is accepted. We will review your request soon.")


# ----------- Запуск обоих ботов -----------
async def main():
    await asyncio.gather(
        dp1.start_polling(bot1),
        dp2.start_polling(bot2)
    )

if __name__ == '__main__':
    asyncio.run(main())
