import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.enums import ParseMode

# Bot token can be obtained via https://t.me/BotFahter
TOKEN = '<your token>'

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(Command('food'))
async def command_start_handler(message: Message) -> None:
    kb = [
        [
            types.KeyboardButton(text='Да😋'),
            types.KeyboardButton(text='Нет😔'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Выберите вариант ответа',
        one_time_keyboard=True
    )
    await message.answer(f'Привет, @{message.from_user.username}, вы будете есть сегодня?', reply_markup=keyboard)


@router.message(Text('Да😋'))
async def text_yes_handler(message: Message) -> None:
    # Send copy of the received message
    await message.answer('Сегодня вы🍖 будете есть✅')


@router.message(Text('Нет😔'))
async def text_no_handler(message: Message) -> None:
    # Send copy of the received message
    await message.answer('Сегодня вы🦴 не будете есть❌')


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode('HTML'))
    # And the run events dispatching
    await dp.start_polling(bot)


def run() -> None:
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


if __name__ == '__main__':
    run()
