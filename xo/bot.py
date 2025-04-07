import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

# Инициализация бота
API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Хранение игр
games = {}

def make_step(game, x, y):
    flag = True
    if game[x][y] == '':
        game[x][y] = 'x'
        flag, message = win_check(game)   
        if flag:
            while True:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if game[x][y] == '':
                    game[x][y] = 'o'
                    flag, message = win_check(game)
                    break  
    else:
        return game, flag, "Эта ячейка уже занята"
    return game, flag, None

def win_check(game):
    # Проверка строк
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != '':
            return False, f'Победил {game[i][0]}!'
        if game[0][i] == game[1][i] == game[2][i] != '':
            return False, f'Победил {game[0][i]}!'
    
    # Проверка диагоналей
    if (game[0][0] == game[1][1] == game[2][2] != '') or \
       (game[0][2] == game[1][1] == game[2][0] != ''):
            return False, f'Победил {game[1][1]}!'
    
    # Проверка на ничью
    if all(cell != '' for row in game for cell in row):
        return False, "Ничья!"
    
    return True, None

def format_board(game):
    board = []
    for i, row in enumerate(game):
        board.append(f"{i} | {' | '.join(cell if cell else ' ' for cell in row)} |")
    return "\n".join(["  0   1   2 ", "  -----------"] + board + ["  -----------"])

@router.message(Command("start", "help"))
async def send_welcome(message: Message):
    await message.reply(
        "Привет! Это игра крестики-нолики.\n"
        "Команды:\n"
        "/newgame - начать новую игру\n"
        "/move X Y - сделать ход (X и Y от 0 до 2)\n"
        "/board - показать текущее поле"
    )

@router.message(Command("newgame"))
async def new_game(message: Message):
    game = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    games[message.chat.id] = {'game': game, 'flag': True}
    await message.reply(
        "Новая игра началась! Вы играете за X.\n"
        f"Текущее поле:\n{format_board(game)}\n"
        "Сделайте ход командой /move X Y (например /move 1 1)"
    )

@router.message(Command("move"))
async def process_move(message: Message):
    chat_id = message.chat.id
    if chat_id not in games or not games[chat_id]['flag']:
        await message.reply("Начните новую игру командой /newgame")
        return
    
    try:
        args = message.text.split()[1:]
        print(args)
        if len(args) != 2:
            raise ValueError
        
        x, y = map(int, args)
        if not (0 <= x <= 2 and 0 <= y <= 2):
            raise ValueError
        
        game_data = games[chat_id]
        game_data['game'], game_data['flag'], error_msg = make_step(game_data['game'], x, y)
        
        if error_msg:
            await message.reply(error_msg)
            return
            
        board_msg = f"Текущее поле:\n{format_board(game_data['game'])}"
        
        if not game_data['flag']:
            _, result_msg = win_check(game_data['game'])
            await message.reply(f"{board_msg}\n{result_msg}\nИгра окончена. Нажми /newgame для новой игры.")
            del games[chat_id]
        else:
            await message.reply(board_msg + "\nОжидаю ваш следующий ход (/move X Y)")
            
    except ValueError:
        await message.reply("Некорректные координаты. Используйте формат /move X Y, где X и Y от 0 до 2")

@router.message(Command("board"))
async def show_board(message: Message):
    chat_id = message.chat.id
    if chat_id not in games:
        await message.reply("Нет активной игры. Начните новую командой /newgame")
        return
    
    await message.reply(f"Текущее поле:\n{format_board(games[chat_id]['game'])}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
