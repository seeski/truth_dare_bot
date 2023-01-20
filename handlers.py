from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU as lex
from keyboards import run_game_kb, game_kb
from services import get_truth, get_dare, get_random



async def start_cmd(message: Message):
    await message.answer(text=lex['hello'], reply_markup=run_game_kb)

async def start_game(message:Message):
    await message.answer(text=lex['game'], reply_markup=game_kb)

async def stop_game(message:Message):
    await message.answer(text=lex['stop_game'], reply_markup=run_game_kb)


async def truth(message: Message):
    truth = get_truth()
    await message.answer(text=truth, reply_markup=game_kb)


async def dare(message: Message):
    dare = get_dare()
    await message.answer(text=dare, reply_markup=game_kb)


async def random(message: Message):
    random = get_random()
    await message.answer(text=random, reply_markup=game_kb)


async def other(message: Message):
    await message.answer(text=lex['other'])

def register_handlers(dp:Dispatcher):
    dp.register_message_handler(start_cmd, commands='start')
    dp.register_message_handler(start_game, text=lex['start_game_button'])
    dp.register_message_handler(stop_game,text=lex['stop_button'])
    dp.register_message_handler(truth, text=lex['truth_button'])
    dp.register_message_handler(dare, text=lex['dare_button'])
    dp.register_message_handler(random, text=lex['random_button'])
    dp.register_message_handler(other)