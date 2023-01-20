from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU as lex

run_game_button = KeyboardButton(lex['start_game_button'])
run_game_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(run_game_button)


truth_button = KeyboardButton(lex['truth_button'])
dare_button = KeyboardButton(lex['dare_button'])
random_button = KeyboardButton(lex['random_button'])
stop_game_button = KeyboardButton(lex['stop_button'])
game_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(truth_button, dare_button, random_button, stop_game_button)
