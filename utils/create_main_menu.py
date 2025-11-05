from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from constants.commands import commands

def create_main_menu(user_lang: str):
  command = commands.get(user_lang, commands['en'])

  main_kb = ReplyKeyboardMarkup(
    keyboard=[
      [
        KeyboardButton(text=command['movie_list']),
        KeyboardButton(text=command['langs']),
        KeyboardButton(text=command['help']),
      ]
    ],
    resize_keyboard=True,   # under the screen
    one_time_keyboard=True # hide after pressing
  )

  return main_kb