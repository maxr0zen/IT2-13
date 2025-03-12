import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Инициализируем бота и диспетчер
bot = Bot(token='your_bot_token_here')  # Замените на ваш токен
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я простой бот на aiogram. Используйте /echo для эхо-ответа.')

# Обработчик команды /echo
@dp.message(Command('echo'))
async def cmd_echo(message: types.Message):
    # Получаем текст после команды /echo
    text = message.text.replace('/echo', '').strip()
    if text:
        await message.answer(text)
    else:
        await message.answer('Пожалуйста, добавьте текст после команды /echo')

# Функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
