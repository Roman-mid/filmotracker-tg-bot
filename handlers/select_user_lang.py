from aiogram import Router, types, F
from .utils import FindCallback
from .tools.user.update_user_lang import update_user_lang
from utils.create_main_menu import create_main_menu
from constants.commands import user_languages
from constants.errors import error

router = Router()

@router.callback_query(FindCallback.filter(F.action == 'update_user_lang'))
async def select_user_lang(call: types.CallbackQuery, callback_data: FindCallback, user):
  await call.message.delete()
  await call.answer() # remove 'clock'

  user_id = user.user_id
  lang = callback_data.lang
  selected_lang = user_languages[lang]['message']

  main_kb = create_main_menu(lang)

  try:
    await update_user_lang(user_id, lang)
    await call.message.answer(text=selected_lang, reply_markup=main_kb)
  except Exception as e:
    lang = user.user_lang
    main_kb = create_main_menu(lang)
    print(f"Ошибка при обровлении языка пользователя (seach_user_lang): {e}")
    print(f"[ERROR], user_id={user_id} {type(e).__name__}: {e}")
    await call.message.answer(text=error[lang], reply_markup=main_kb, parse_mode='HTML')

  



