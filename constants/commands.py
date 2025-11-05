commands = {
  "en": {"movie_list": "My Movies", "langs": "Change Language", "help": "Help"},
  "ru": {"movie_list": "Мои фильмы", "langs": "Сменить язык", "help": "Помощь"},
  "uk": {"movie_list": "Мої фільми", "langs": "Змінити мову", "help": "Допомога"},
  "ar": {"movie_list": "أفلامي", "langs": "تغيير اللغة", "help": "مساعدة"},
  "fr": {"movie_list": "Mes films", "langs": "Changer la langue", "help": "Aide"},
  "de": {"movie_list": "Meine Filme", "langs": "Sprache ändern", "help": "Hilfe"},
  "it": {"movie_list": "I miei film", "langs": "Cambia lingua", "help": "Aiuto"},
  "ko": {"movie_list": "내 영화", "langs": "언어 변경", "help": "도움말"},
  "pl": {"movie_list": "Moje filmy", "langs": "Zmień język", "help": "Pomoc"},
  "pr-br": {"movie_list": "Meus filmes", "langs": "Mudar idioma", "help": "Ajuda"},
  "es": {"movie_list": "Mis películas", "langs": "Cambiar idioma", "help": "Ayuda"},
  "tr": {"movie_list": "Filmlerim", "langs": "Dili değiştir", "help": "Yardım"},
  "cs": {"movie_list": "Moje filmy", "langs": "Změnit jazyk", "help": "Nápověda"},
  "nl": {"movie_list": "Mijn films", "langs": "Taal wijzigen", "help": "Help"},
  "hu": {"movie_list": "Filmjeim", "langs": "Nyelv módosítása", "help": "Súgó"},
  "nb": {"movie_list": "Mine filmer", "langs": "Bytt språk", "help": "Hjelp"},
  "sv": {"movie_list": "Mina filmer", "langs": "Byt språk", "help": "Hjälp"}
}


movie_list_tuple = tuple(v['movie_list'] for v in commands.values())
langs_tuple = tuple(v['langs'] for v in commands.values())
help_tuple = tuple(v['help'] for v in commands.values())

user_languages = {
    "en": {"label": "English", "message": "Interface language changed", "title": "Select language"},
    "ru": {"label": "Русский", "message": "Язык интерфейса изменен", "title": "Выберите язык"},
    "uk": {"label": "Українська", "message": "Мову інтерфейсу змінено", "title": "Виберіть мову"},
    "ar": {"label": "العربية", "message": "تم تغيير لغة الواجهة", "title": "اختر اللغة"},
    "fr": {"label": "Français", "message": "Langue de l’interface modifiée", "title": "Sélectionnez la langue"},
    "de": {"label": "Deutsch", "message": "Sprache der Benutzeroberfläche geändert", "title": "Sprache auswählen"},
    "it": {"label": "Italiano", "message": "Lingua dell'interfaccia modificata", "title": "Seleziona la lingua"},
    "ko": {"label": "한국어", "message": "인터페이스 언어가 변경되었습니다", "title": "언어 선택"},
    "pl": {"label": "Polski", "message": "Zmieniono język interfejsu", "title": "Wybierz język"},
    "pr-br": {"label": "Português (Brasil)", "message": "Idioma da interface alterado", "title": "Selecione o idioma"},
    "es": {"label": "Español", "message": "Idioma de la interfaz cambiado", "title": "Selecciona el idioma"},
    "tr": {"label": "Türkçe", "message": "Arayüz dili değiştirildi", "title": "Dil seçin"},
    "cs": {"label": "Čeština", "message": "Jazyk rozhraní byl změněn", "title": "Vyberte jazyk"},
    "nl": {"label": "Nederlands", "message": "Taal van de interface gewijzigd", "title": "Selecteer taal"},
    "hu": {"label": "Magyar", "message": "A felület nyelve megváltozott", "title": "Válasszon nyelvet"},
    "nb": {"label": "Norsk Bokmål", "message": "Grensesnittspråket er endret", "title": "Velg språk"},
    "sv": {"label": "Svenska", "message": "Gränssnittsspråket har ändrats", "title": "Välj språk"}
}
