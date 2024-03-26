import requests
url = 'https://v6.exchangerate-api.com/v6/7688eb57ddaadf00f5301196/latest/USD'
requests.get(url)
# print(b.json()['conversion_rate'])
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
TOKEN = "6536998976:AAGzSIbowQK4Fxga-cUcdxqTgmeIFAcbk50"
dp = Dispatcher()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    a=[
        [
            types.KeyboardButton(text="USD"),
            types.KeyboardButton(text="EUR"),
            types.KeyboardButton(text="AED"),
        ]
    ]
    markup=types.ReplyKeyboardMarkup(keyboard=a,resize_keyboard=True)
    await message.answer(f"Horijiz valyutani oz'bek so'miga otqizberuvchi botga xush kelbisiz, {hbold(message.from_user.full_name)}!\n"
                         f"Quyidagi buttonlar yoki oz'ingiz keralki bolgan valyutani yozib  valyutani ozbek so'midagi narxini bilib olish uchun ishlating!\nMasalan:EUR",reply_markup=markup)
@dp.message()
async def valyuta(message:Message):
    try:
        text = message.text
        a = f"https://v6.exchangerate-api.com/v6/7688eb57ddaadf00f5301196/pair/{text}/UZS"
        b = requests.get(a)
        await message.answer(f"{b.json()['conversion_rate']} UZS")
    except:
        await message.answer("Listda mavjud bolmagan valyuta kiritildi!")
async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
