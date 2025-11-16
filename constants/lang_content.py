lang_content = {
    # english  
    'en': {
        'button': {
            'providers': 'Providers',
            'remove': 'Remove',
            "remove_from": "Remove from library",
            "add": "Add to library",
            'details': 'Details',
            'languages': 'Languages',
            'trailer': 'Trailer',
            'find_movie': 'Find a movie',
            'find_tv': 'Find a TV serial',
            'subscribe': 'Subscribe'
        },
        'message': {
            'not_found': 'Not found', 
            'no_descriptions': 'No descriptions',
            'no_information_available': 'No information available'
        },
        'stop': {
          'first': 'Don`t do it again.',
          'second': '❌ STOP IT.',
          'third': '❌ STO-O-OP IT !!!',
          'last': 'Please, stop it. Please... '
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Providers:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 Languages available:\n\n{langs_text}',
        'release': {
          'new_episod': '❗ New episode released.',
          'movie': lambda title: f'❗ <b>{title}</b> was released today!'
        },
        'trailer': {
          'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
          'not_awailable': 'No trailer available'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> is added to your library",
            'already_added': lambda title: f"✅ <b>{title}</b> is already in your library",
        },
        "follow_list": {
            "title": "🎬 <b><i>Your library:</i></b> \n",
            "not_found_in_list": "❌ Error. Movie is not found in your library.",
            "empty_list": "<b><i>Your library is empty.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> is removed from your library",
            "already_removed": "You have already removed this movie",
        },
        'payment': {
          'title': 'Select the payment sistem:',
          'session_completed': '✅ We are processing your payment. It can take some time.',
          'payment_succeeded': '✅ Payment successful, subscription activated!',
          'payment_failed': '⚠️ Your subscription payment failed. Please check your card.',
          'stop': '✅ Your subscription will be canceled at the end of the paid period.',
          'fail_stop': '❌ Failed to cancel the subscription. Please try again later.',
          'subscription_deleted': '❌ Your subscription is no longer active.',
          'not_found': '⚠️ You don’t have any active subscriptions',
          'subscription_expired': (
                '❌ <b>Your subscription has expired.</b>\n'
                'If you want to get new notifications, please click the button 👇'
            )
        },
        'movie_info': {
            'seasons': 'Seasons:',
            'current_season': 'Current season',
            'number_of_episodes': 'Number of episodes:',
            'episodes': 'Episodes:',
            'last_episode': 'Last episode:',
            'next_episod_date': 'Next episode:',
            'genre': 'Genre:',
            'release': '📅 Release:',
            'rating': '⭐ Rating:',
            "already_added": "already in your library",

        },
        'next_episode_info': {
          'title': 'Title',
          'season_number': 'Season',
          'episode_number': 'Episode',
        }
    },
    # russian
    'ru': {
        'button': {
            'providers': 'Провайдеры',
            'remove': 'Удалить',
            "remove_from": "Удалить из библиотеки",
            "add": "Добавить в библиотеку",
            'details': 'Подробнее',
            'languages': 'Языки',
            'trailer': 'Трейлер',
            'find_movie': 'Найти фильм',
            'find_tv': 'Найти сериал',
            'subscribe': 'Подписаться'
        },
        'message': {
            'not_found': 'Не найдено',
            'no_descriptions': 'Нет описаний',
            'no_information_available': 'Информация недоступна'
        },
        'stop': {
            'first': 'Не делайте так больше.',
            'second': '❌ ХВАТИТ.',
            'third': '❌ ХВА-А-А-А-ТИТ !!!',
            'last': 'Хватит. Я прошу тебя, хватит... '
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Провайдеры:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Доступные языки:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Вышла новая серия.",
            "movie": lambda title: f"❗ <b>{title}</b> вышел сегодня!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Трейлер: {trailer_url}',
            'not_awailable': 'Трейлер недоступен'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> добавлен в вашу библиотеку",
            'already_added': lambda title: f"✅ <b>{title}</b> уже есть в вашей библиотеке",
        },
        "follow_list": {
            "title": "🎬 <b><i>Ваша библиотека:</i></b> \n",
            "not_found_in_list": "❌ Ошибка. Фильм не найден в вашей библиотеке.",
            "empty_list": "<b><i>Ваша библиотека пуста.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> удалён из вашей библиотеки",
            "already_removed": "Вы уже удалили этот фильм",
        },
        'payment': {
            'title': 'Выберите систему оплаты:',
            'session_completed': '✅ Мы обрабатываем ваш платеж. Это может занять некоторое время.',
            'stop': '✅ Ваша подписка будет отменена в конце оплаченного периода.',
            'fail_stop': '❌ Не удалось отменить подписку. Попробуйте позже.',
            'payment_succeeded': '✅ Оплата успешна, подписка активирована!',
            'payment_failed': '⚠️ Оплата подписки не прошла. Проверьте карту.',
            'subscription_deleted': '❌ Ваша подписка завершена.',
            'not_found': '⚠️ У вас нет активных подписок',
            'subscription_expired': (
                '❌ <b>Ваша подписка истекла.</b>\n'
                'Если хотите получать новые уведомления, нажмите кнопку ниже 👇'
            )
        },
        "movie_info": {
            "seasons": "Сезоны:",
            "current_season": "Текущий сезон",
            "number_of_episodes": "Количество эпизодов:",
            "episodes": "Эпизоды:",
            "last_episode": "Последний эпизод:",
            "next_episod_date": "Следующий эпизод:",
            "genre": "Жанр:",
            "release": "📅 Дата выхода:",
            "rating": "⭐ Рейтинг:",
            "already_added": "уже в вашей библиотеке",
        },
        "next_episode_info": {
            "title": "Название",
            "season_number": "Сезон",
            "episode_number": "Эпизод",
        },
    },
    # ukrainian
    'uk': {
        'button': {
           'providers': 'Провайдери',
            'remove': 'Видалити',
            "remove_from": "Видалити з бібліотеки",
            "add": "Додати до бібліотеки",
            'details': 'Деталі',
            'languages': 'Мови',
            'trailer': 'Трейлер',
            'find_movie': 'Знайти фільм',
            'find_tv': 'Знайти серіал',
            'subscribe': 'Підписатися'
        },
        'message': {
            'not_found': 'Не знайдено', 
            'no_descriptions': 'Немає описів',
            'no_information_available': 'Інформація недоступна'
        },
        'stop': {
            'first': 'Не роби так більше.',
            'second': '❌ ДОСИТЬ.',
            'third': '❌ ПРИ-И-ПИ-НИ !!!',
            'last': 'Будь людиною, схаменись. Благаю...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Провайдери:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬<b>Доступні мови:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Вийшов новий епізод.",
            "movie": lambda title: f"❗ <b>{title}</b> вийшов сьогодні!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Трейлер: {trailer_url}',
            'not_awailable': 'Трейлер недоступний'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> додано до вашої бібліотеки",
            'already_added': lambda title: f"✅ <b>{title}</b> вже є у вашій бібліотеці",
        },
        "follow_list": {
            "title": "🎬 <b><i>Ваша бібліотека:</i></b> \n",
            "not_found_in_list": "❌ Помилка. Фільм не знайдено у вашій бібліотеці.",
            "empty_list": "<b><i>Ваша бібліотека порожня.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> видалено з вашої бібліотеки",
            "already_removed": "Ви вже видалили цей фільм",
        },
        'payment': {
            'title': 'Виберіть платіжну систему:',
            'session_completed': '✅ Ми обробляємо ваш платіж. Це може зайняти деякий час.',
            'payment_succeeded': '✅ Платіж успішний, підписка активована!',
            'payment_failed': '⚠️ Платіж по вашій підписці не пройшов. Перевірте вашу карту.',
            'stop': '✅ Ваша підписка буде скасована в кінці оплаченного періоду.',
            'fail_stop': '❌ Не вдалося скасувати підписку. Спробуйте пізніше.',
            'subscription_deleted': '❌ Ваша підписка більше не активна.',
            'not_found': '⚠️ У вас немає активних підписок',
            'subscription_expired': (
                '❌ <b>Ваша підписка закінчилася.</b>\n'
                'Якщо ви хочете отримувати нові сповіщення, натисніть кнопку нижче 👇'
            )
        },
        "movie_info": {
            "seasons": "Сезони:",
            "current_season": "Поточний сезон",
            "number_of_episodes": "Кількість епізодів:",
            "episodes": "Епізоди:",
            "last_episode": "Останній епізод:",
            "next_episod_date": "Наступний епізод:",
            "genre": "Жанр:",
            "release": "📅 Дата виходу:",
            "rating": "⭐ Рейтинг:",
            "already_added": "вже у вашій бібліотеці",
        },
        "next_episode_info": {
            "title": "Назва",
            "season_number": "Сезон",
            "episode_number": "Епізод",
        },
    },
    # arabic
    'ar': {
        'button': {
           'providers': 'المزوّدون',
            'remove': 'حذف',
            "remove_from": "إزالة من المكتبة",
            "add": "إضافة إلى المكتبة",
            'details': 'تفاصيل',
            'languages': 'اللغات',
            'trailer': 'المقطع الدعائي',
            'find_movie': 'ابحث عن فيلم',
            'find_tv': 'ابحث عن مسلسل',
            'subscribe': 'اشترك'
        },
        'message': {
            'not_found': 'لم يتم العثور عليه',
            'no_descriptions': 'لا توجد أوصاف',
            'no_information_available': 'لا تتوفر معلومات'
        },
        'stop': {
            'first': 'لا تفعل ذلك مرة أخرى.',
            'second': '❌ توقف عن ذلك.',
            'third': '❌ توقّف-وا-أوقف !!!',
            'last': 'من فضلك، توقف. من فضلك...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>الموفرون:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>اللغات المتاحة:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ تم إصدار حلقة جديدة.",
            "movie": lambda title: f"❗ <b>{title}</b> تم إصداره اليوم!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 المقطع الدعائي: {trailer_url}',
            'not_awailable': 'المقطع الدعائي غير متوفر'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> تم إضافته إلى مكتبتك",
            'already_added': lambda title: f"✅ <b>{title}</b> موجود بالفعل في مكتبتك",
        },
        "follow_list": {
            "title": "🎬 <b><i>مكتبتك:</i></b> \n",
            "not_found_in_list": "❌ خطأ. الفيلم غير موجود في مكتبتك.",
            "empty_list": "<b><i>مكتبتك فارغة.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> تمت إزالته من مكتبتك",
            "already_removed": "لقد قمت بإزالة هذا الفيلم بالفعل",
        },
        'payment': {
            'title': 'اختر طريقة الدفع:',
            'session_completed': '✅ نحن نقوم بمعالجة الدفع. قد يستغرق بعض الوقت.',
            'payment_succeeded': '✅ تم الدفع بنجاح، وتم تفعيل الاشتراك!',
            'payment_failed': '⚠️ فشل دفع الاشتراك. يرجى التحقق من بطاقتك.',
            'stop': '✅ سيتم إلغاء اشتراكك في نهاية الفترة المدفوعة.',
            'fail_stop': '❌ فشل في إلغاء الاشتراك. يرجى المحاولة لاحقاً.',
            'subscription_deleted': '❌ اشتراكك لم يعد نشطاً.',
            'not_found': '⚠️ ليس لديك أي اشتراكات نشطة',
            'subscription_expired': (
                '❌ <b>انتهت صلاحية اشتراكك.</b>\n'
                'إذا كنت ترغب في تلقي إشعارات جديدة، يرجى الضغط على الزر أدناه 👇'
            )
        },
        "movie_info": {
            "seasons": "المواسم:",
            "current_season": "الموسم الحالي",
            "number_of_episodes": "عدد الحلقات:",
            "episodes": "الحلقات:",
            "last_episode": "الحلقة الأخيرة:",
            "next_episod_date": "الحلقة التالية:",
            "genre": "النوع:",
            "release": "📅 تاريخ الإصدار:",
            "rating": "⭐ التقييم:",
            "already_added": "موجود بالفعل في مكتبتك",
        },
        "next_episode_info": {
            "title": "العنوان",
            "season_number": "الموسم",
            "episode_number": "الحلقة",
        },
    },
    # french
    'fr': {
        'button': {
           'providers': 'Fournisseurs',
            'remove': 'Supprimer',
            "remove_from": "Supprimer de la bibliothèque",
            "add": "Ajouter à la bibliothèque",
            'details': 'Détails',
            'languages': 'Langues',
            'trailer': 'Bande-annonce',
            'find_movie': 'Trouver un film',
            'find_tv': 'Trouver une série TV',
            'subscribe': "S'abonner"
        },
        'message': {
            'not_found': 'Non trouvé',
            'no_descriptions': 'Pas de descriptions',
            'no_information_available': 'Aucune information disponible'
        },
        'stop': {
            'first': 'Ne refaites pas ça.',
            'second': '❌ ARRÊTEZ.',
            'third': '❌ ARRÊTEEEZ !!!',
            'last': 'S’il vous plaît, arrêtez. S’il vous plaît...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Fournisseurs :</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Langues disponibles:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nouvel épisode disponible.",
            "movie": lambda title: f"❗ <b>{title}</b> est sorti aujourd’hui!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Bande-annonce : {trailer_url}',
            'not_awailable': 'Bande-annonce non disponible'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> a été ajouté à votre bibliothèque",
            'already_added': lambda title: f"✅ <b>{title}</b> est déjà dans votre bibliothèque",
        },
        "follow_list": {
            "title": "🎬 <b><i>Votre bibliothèque :</i></b> \n",
            "not_found_in_list": "❌ Erreur. Le film n'a pas été trouvé dans votre bibliothèque.",
            "empty_list": "<b><i>Votre bibliothèque est vide.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> a été supprimé de votre bibliothèque",
            "already_removed": "Vous avez déjà supprimé ce film",
        },
        'payment': {
            'title': 'Sélectionnez le système de paiement :',
            'session_completed': '✅ Nous traitons votre paiement. Cela peut prendre un certain temps.',
            'payment_succeeded': '✅ Paiement réussi, abonnement activé !',
            'payment_failed': '⚠️ Le paiement de votre abonnement a échoué. Veuillez vérifier votre carte.',
            'stop': '✅ Votre abonnement sera annulé à la fin de la période payée.',
            'fail_stop': '❌ Échec de l’annulation de l’abonnement. Veuillez réessayer plus tard.',
            'subscription_deleted': '❌ Votre abonnement n’est plus actif.',
            'not_found': '⚠️ Vous n’avez aucun abonnement actif',
            'subscription_expired': (
                '❌ <b>Votre abonnement a expiré.</b>\n'
                'Si vous souhaitez recevoir de nouvelles notifications, veuillez cliquer sur le bouton ci-dessous 👇'
            )
        },
        "movie_info": {
            "seasons": "Saisons:",
            "current_season": "Saison actuelle",
            "number_of_episodes": "Nombre d’épisodes:",
            "episodes": "Épisodes:",
            "last_episode": "Dernier épisode:",
            "next_episod_date": "Prochain épisode:",
            "genre": "Genre:",
            "release": "📅 Sortie:",
            "rating": "⭐ Note:",
            "already_added": "déjà dans ta bibliothèque",
        },
        "next_episode_info": {
            "title": "Titre",
            "season_number": "Saison",
            "episode_number": "Épisode",
        },
    },
    # german
    'de': {
        'button': {
           'providers': 'Anbieter',
            'remove': 'Entfernen',
            "remove_from": "Aus der Bibliothek entfernen",
            "add": "Zur Bibliothek hinzufügen",
            'details': 'Details',
            'languages': 'Sprachen',
            'trailer': 'Trailer',
            'find_movie': 'Film finden',
            'find_tv': 'Serie finden',
            'subscribe': 'Abonnieren'
        },
        'message': {
            'not_found': 'Nicht gefunden',
            'no_descriptions': 'Keine Beschreibungen',
            'no_information_available': 'Keine Informationen verfügbar'
        },
        'stop': {
            'first': 'Mach das nicht noch einmal.',
            'second': '❌ HÖR AUF.',
            'third': '❌ HÖR AUUUF !!!',
            'last': 'Bitte hör auf. Bitte...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Anbieter:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Verfügbare Sprachen:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Neue Folge veröffentlicht.",
            "movie": lambda title: f"❗ <b>{title}</b> wurde heute veröffentlicht!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
            'not_awailable': 'Kein Trailer verfügbar'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> wurde deiner Bibliothek hinzugefügt",
            'already_added': lambda title: f"✅ <b>{title}</b> befindet sich bereits in Ihrer Bibliothek",
        },
        "follow_list": {
            "title": "🎬 <b><i>Deine Bibliothek:</i></b> \n",
            "not_found_in_list": "❌ Fehler. Film nicht in deiner Bibliothek gefunden.",
            "empty_list": "<b><i>Deine Bibliothek ist leer.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> wurde aus deiner Bibliothek entfernt",
            "already_removed": "Du hast diesen Film bereits entfernt",
        },
        'payment': {
            'title': 'Wählen Sie das Zahlungssystem:',
            'session_completed': '✅ Wir verarbeiten Ihre Zahlung. Dies kann einige Zeit dauern.',
            'payment_succeeded': '✅ Zahlung erfolgreich, Abonnement aktiviert!',
            'payment_failed': '⚠️ Ihre Abonnementzahlung ist fehlgeschlagen. Bitte überprüfen Sie Ihre Karte.',
            'stop': '✅ Ihr Abonnement wird am Ende des bezahlten Zeitraums gekündigt.',
            'fail_stop': '❌ Kündigung des Abonnements fehlgeschlagen. Bitte versuchen Sie es später erneut.',
            'subscription_deleted': '❌ Ihr Abonnement ist nicht mehr aktiv.',
            'not_found': '⚠️ Sie haben keine aktiven Abonnements',
            'subscription_expired': (
                '❌ <b>Ihr Abonnement ist abgelaufen.</b>\n'
                'Wenn Sie neue Benachrichtigungen erhalten möchten, klicken Sie bitte auf die Schaltfläche unten 👇'
            )
        },
        "movie_info": {
            "seasons": "Staffeln:",
            "current_season": "Aktuelle Staffel",
            "number_of_episodes": "Anzahl der Episoden:",
            "episodes": "Episoden:",
            "last_episode": "Letzte Episode:",
            "next_episod_date": "Nächste Episode:",
            "genre": "Genre:",
            "release": "📅 Veröffentlichung:",
            "rating": "⭐ Bewertung:",
            "already_added": "bereits in deiner Bibliothek",
        },
        "next_episode_info": {
            "title": "Titel",
            "season_number": "Staffel",
            "episode_number": "Episode",
        },
    },
    # italian
    'it': {
        'button': {
           'providers': 'Fornitori',
            'remove': 'Rimuovi',
            "remove_from": "Rimuovi dalla libreria",
            "add": "Aggiungi alla libreria",
            'details': 'Dettagli',
            'languages': 'Lingue',
            'trailer': 'Trailer',
            'find_movie': 'Trova un film',
            'find_tv': 'Trova una serie TV',
            'subscribe': 'Iscriviti'
        },
        'message': {
            'not_found': 'Non trovato',
            'no_descriptions': 'Nessuna descrizione',
            'no_information_available': 'Informazioni non disponibili'
        },
        'stop': {
            'first': 'Non farlo di nuovo.',
            'second': '❌ FERMA!',
            'third': '❌ FEEERMA !!!',
            'last': 'Per favore, fermati. Per favore...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Fornitori:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Lingue disponibili:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nuovo episodio rilasciato.",
            "movie": lambda title: f"❗ <b>{title}</b> è stato rilasciato oggi!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
            'not_awailable': 'Trailer non disponibile'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> è stato aggiunto alla tua libreria",
            'already_added': lambda title: f"✅ <b>{title}</b> è già nella tua libreria",
        },
        "follow_list": {
            "title": "🎬 <b><i>La tua libreria:</i></b> \n",
            "not_found_in_list": "❌ Errore. Film non trovato nella tua libreria.",
            "empty_list": "<b><i>La tua libreria è vuota.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> è stato rimosso dalla tua libreria",
            "already_removed": "Hai già rimosso questo film",
        },
        'payment': {
            'title': 'Seleziona il metodo di pagamento:',
            'session_completed': '✅ Stiamo elaborando il tuo pagamento. Potrebbe richiedere un po’ di tempo.',
            'payment_succeeded': '✅ Pagamento riuscito, abbonamento attivato!',
            'payment_failed': '⚠️ Il pagamento del tuo abbonamento è fallito. Controlla la tua carta.',
            'stop': '✅ Il tuo abbonamento sarà annullato alla fine del periodo pagato.',
            'fail_stop': '❌ Impossibile annullare l’abbonamento. Riprova più tardi.',
            'subscription_deleted': '❌ Il tuo abbonamento non è più attivo.',
            'not_found': '⚠️ Non hai abbonamenti attivi',
            'subscription_expired': (
                '❌ <b>Il tuo abbonamento è scaduto.</b>\n'
                'Se vuoi ricevere nuove notifiche, premi il pulsante qui sotto 👇'
            )
        },
        "movie_info": {
            "seasons": "Stagioni:",
            "current_season": "Stagione attuale",
            "number_of_episodes": "Numero di episodi:",
            "episodes": "Episodi:",
            "last_episode": "Ultimo episodio:",
            "next_episod_date": "Prossimo episodio:",
            "genre": "Genere:",
            "release": "📅 Uscita:",
            "rating": "⭐ Valutazione:",
            "already_added": "già nella tua libreria",
        },
        "next_episode_info": {
            "title": "Titolo",
            "season_number": "Stagione",
            "episode_number": "Episodio",
        },
    },
    # korean
    'ko': {
        'button': {
           'providers': '공급자',
            'remove': '제거',
            "remove_from": "라이브러리에서 제거",
            "add": "라이브러리에 추가",
            'details': '세부 정보',
            'languages': '언어',
            'trailer': '예고편',
            'find_movie': '영화 찾기',
            'find_tv': 'TV 시리즈 찾기',
            'subscribe': '구독하기'
        },
        'message': {
            'not_found': '찾을 수 없음',
            'no_descriptions': '설명이 없음',
            'no_information_available': '사용 가능한 정보가 없습니다'
        },
        'stop': {
            'first': '다시는 그렇게 하지 마세요.',
            'second': '❌ 그만하세요.',
            'third': '❌ 그만-멈-춰 !!!',
            'last': '제발, 멈춰 주세요. 제발...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>제공사:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>사용 가능한 언어:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ 새로운 에피소드가 출시되었습니다.",
            "movie": lambda title: f"❗ <b>{title}</b> 오늘 출시되었습니다!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 예고편: {trailer_url}',
            'not_awailable': '예고편을 사용할 수 없습니다'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> 라이브러리에 추가되었습니다",
            'already_added': lambda title: f"✅ <b>{title}</b> 이미 내 라이브러리에 있습니다",
        },
        "follow_list": {
            "title": "🎬 <b><i>내 라이브러리:</i></b> \n",
            "not_found_in_list": "❌ 오류. 영화가 라이브러리에 없습니다.",
            "empty_list": "<b><i>라이브러리가 비어 있습니다.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> 라이브러리에서 제거되었습니다",
            "already_removed": "이미 이 영화를 제거했습니다",
        },
        'payment': {
            'title': '결제 시스템 선택:',
            'session_completed': '✅ 결제를 처리 중입니다. 잠시 시간이 걸릴 수 있습니다.',
            'payment_succeeded': '✅ 결제 성공, 구독이 활성화되었습니다!',
            'payment_failed': '⚠️ 구독 결제 실패. 카드 정보를 확인해주세요.',
            'stop': '✅ 유료 기간 종료 시 구독이 취소됩니다.',
            'fail_stop': '❌ 구독 취소에 실패했습니다. 나중에 다시 시도해주세요.',
            'subscription_deleted': '❌ 구독이 더 이상 활성화되지 않았습니다.',
            'not_found': '⚠️ 활성 구독이 없습니다',
            'subscription_expired': (
                '❌ <b>구독이 만료되었습니다.</b>\n'
                '새 알림을 받으시려면 아래 버튼을 눌러주세요 👇'
            )
        },
        "movie_info": {
            "seasons": "시즌:",
            "current_season": "현재 시즌",
            "number_of_episodes": "에피소드 수:",
            "episodes": "에피소드:",
            "last_episode": "마지막 에피소드:",
            "next_episod_date": "다음 에피소드:",
            "genre": "장르:",
            "release": "📅 출시일:",
            "rating": "⭐ 평점:",
            "already_added": "이미 라이브러리에 있습니다",
        },
        "next_episode_info": {
            "title": "제목",
            "season_number": "시즌",
            "episode_number": "에피소드",
        },
    },
    # polish
    'pl': {
        'button': {
           'providers': 'Dostawcy',
            'remove': 'Usuń',
            "remove_from": "Usuń z biblioteki",
            "add": "Dodaj do biblioteki",
            'details': 'Szczegóły',
            'languages': 'Języki',
            'trailer': 'Zwiastun',
            'find_movie': 'Znajdź film',
            'find_tv': 'Znajdź serial',
            'subscribe': 'Subskrybuj'
        },
        'message': {
            'not_found': 'Nie znaleziono',
            'no_descriptions': 'Brak opisów',
            'no_information_available': 'Brak dostępnych informacji'
        },
        'stop': {
            'first': 'Nie rób tego ponownie.',
            'second': '❌ PRZESTAŃ.',
            'third': '❌ PRZE-STA-Ń !!!',
            'last': 'Proszę, przestań. Proszę...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Dostawcy:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Dostępne języki:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nowy odcinek wydany.",
            "movie": lambda title: f"❗ <b>{title}</b> miał dziś premierę!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Zwiastun: {trailer_url}',
            'not_awailable': 'Zwiastun niedostępny'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> został dodany do twojej biblioteki",
            'already_added': lambda title: f"✅ <b>{title}</b> jest już w twojej bibliotece",
        },
        "follow_list": {
            "title": "🎬 <b><i>Twoja biblioteka:</i></b> \n",
            "not_found_in_list": "❌ Błąd. Film nie został znaleziony w twojej bibliotece.",
            "empty_list": "<b><i>Twoja biblioteka jest pusta.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> został usunięty z twojej biblioteki",
            "already_removed": "Już usunąłeś ten film",
        },
        'payment': {
            'title': 'Wybierz system płatności:',
            'session_completed': '✅ Przetwarzamy twoją płatność. Może to chwilę potrwać.',
            'payment_succeeded': '✅ Płatność zakończona sukcesem, subskrypcja aktywowana!',
            'payment_failed': '⚠️ Płatność subskrypcji nie powiodła się. Sprawdź kartę.',
            'stop': '✅ Twoja subskrypcja zostanie anulowana po zakończeniu opłaconego okresu.',
            'fail_stop': '❌ Nie udało się anulować subskrypcji. Spróbuj ponownie później.',
            'subscription_deleted': '❌ Twoja subskrypcja nie jest już aktywna.',
            'not_found': '⚠️ Nie masz aktywnych subskrypcji',
            'subscription_expired': (
                '❌ <b>Twoja subskrypcja wygasła.</b>\n'
                'Jeśli chcesz otrzymywać nowe powiadomienia, kliknij przycisk poniżej 👇'
            )
        },
        "movie_info": {
            "seasons": "Sezony:",
            "current_season": "Bieżący sezon",
            "number_of_episodes": "Liczba odcinków:",
            "episodes": "Odcinki:",
            "last_episode": "Ostatni odcinek:",
            "next_episod_date": "Następny odcinek:",
            "genre": "Gatunek:",
            "release": "📅 Premiera:",
            "rating": "⭐ Ocena:",
            "already_added": "już w twojej bibliotece",
        },
        "next_episode_info": {
            "title": "Tytuł",
            "season_number": "Sezon",
            "episode_number": "Odcinek",
        },
    },
    # portuguese - brasil
    'pt-br': {
        'button': {
           'providers': 'Provedores',
            'remove': 'Remover',
            "remove_from": "Remover da biblioteca",
            "add": "Adicionar à biblioteca",
            'details': 'Detalhes',
            'languages': 'Idiomas',
            'trailer': 'Trailer',
            'find_movie': 'Encontrar um filme',
            'find_tv': 'Encontrar uma série de TV',
            'subscribe': 'Inscrever-se'
        },
        'message': {
            'not_found': 'Não encontrado',
            'no_descriptions': 'Sem descrições',
            'no_information_available': 'Informações não disponíveis'
        },
        'stop': {
            'first': 'Não faça isso novamente.',
            'second': '❌ PARE COM ISSO.',
            'third': '❌ PAAARAR !!!',
            'last': 'Por favor, pare. Por favor...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Provedores:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Idiomas disponíveis:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Novo episódio lançado.",
            "movie": lambda title: f"❗ <b>{title}</b> foi lançado hoje!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
            'not_awailable': 'Trailer não disponível'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> foi adicionado à sua biblioteca",
            'already_added': lambda title: f"✅ <b>{title}</b> já está na sua biblioteca",
        },
        "follow_list": {
            "title": "🎬 <b><i>Sua biblioteca:</i></b> \n",
            "not_found_in_list": "❌ Erro. Filme não encontrado na sua biblioteca.",
            "empty_list": "<b><i>Sua biblioteca está vazia.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> foi removido da sua biblioteca",
            "already_removed": "Você já removeu este filme",
        },
        'payment': {
            'title': 'Selecione o sistema de pagamento:',
            'session_completed': '✅ Estamos processando seu pagamento. Isso pode levar algum tempo.',
            'payment_succeeded': '✅ Pagamento realizado com sucesso, assinatura ativada!',
            'payment_failed': '⚠️ Falha no pagamento da assinatura. Verifique seu cartão.',
            'stop': '✅ Sua assinatura será cancelada ao final do período pago.',
            'fail_stop': '❌ Falha ao cancelar a assinatura. Tente novamente mais tarde.',
            'subscription_deleted': '❌ Sua assinatura não está mais ativa.',
            'not_found': '⚠️ Você não possui assinaturas ativas',
            'subscription_expired': (
                '❌ <b>Sua assinatura expirou.</b>\n'
                'Se deseja receber novas notificações, clique no botão abaixo 👇'
            )
        },
        "movie_info": {
            "seasons": "Temporadas:",
            "current_season": "Temporada atual",
            "number_of_episodes": "Número de episódios:",
            "episodes": "Episódios:",
            "last_episode": "Último episódio:",
            "next_episod_date": "Próximo episódio:",
            "genre": "Gênero:",
            "release": "📅 Lançamento:",
            "rating": "⭐ Avaliação:",
            "already_added": "já está na sua biblioteca",
        },
        "next_episode_info": {
            "title": "Título",
            "season_number": "Temporada",
            "episode_number": "Episódio",
        },
    },
    # spain
    'es': {
        'button': {
           'providers': 'Proveedores',
            'remove': 'Eliminar',
            "remove_from": "Eliminar de la biblioteca",
            "add": "Agregar a la biblioteca",
            'details': 'Detalles',
            'languages': 'Idiomas',
            'trailer': 'Tráiler',
            'find_movie': 'Buscar una película',
            'find_tv': 'Buscar una serie de TV',
            'subscribe': 'Suscribirse'
        },
        'message': {
            'not_found': 'No encontrado',
            'no_descriptions': 'Sin descripciones',
            'no_information_available': 'No hay información disponible'
        },
        'stop': {
            'first': 'No lo hagas de nuevo.',
            'second': '❌ DETÉNLO.',
            'third': '❌ DETEEENLO !!!',
            'last': 'Por favor, detente. Por favor...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Proveedores:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Idiomas disponibles:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nuevo episodio disponible.",
            "movie": lambda title: f"❗ <b>{title}</b> se estrenó hoy!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Tráiler: {trailer_url}',
            'not_awailable': 'Tráiler no disponible'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> se ha agregado a tu biblioteca",
            'already_added': lambda title: f"✅ <b>{title}</b> ya está en tu biblioteca",
        },
        "follow_list": {
            "title": "🎬 <b><i>Tu biblioteca:</i></b> \n",
            "not_found_in_list": "❌ Error. Película no encontrada en tu biblioteca.",
            "empty_list": "<b><i>Tu biblioteca está vacía.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> ha sido eliminada de tu biblioteca",
            "already_removed": "Ya has eliminado esta película",
        },
        'payment': {
            'title': 'Selecciona el sistema de pago:',
            'session_completed': '✅ Estamos procesando tu pago. Esto puede tomar algún tiempo.',
            'payment_succeeded': '✅ Pago exitoso, ¡suscripción activada!',
            'payment_failed': '⚠️ Falló el pago de tu suscripción. Verifica tu tarjeta.',
            'stop': '✅ Tu suscripción se cancelará al final del período pagado.',
            'fail_stop': '❌ No se pudo cancelar la suscripción. Por favor, inténtalo más tarde.',
            'subscription_deleted': '❌ Tu suscripción ya no está activa.',
            'not_found': '⚠️ No tienes suscripciones activas',
            'subscription_expired': (
                '❌ <b>Tu suscripción ha expirado.</b>\n'
                'Si deseas recibir nuevas notificaciones, haz clic en el botón de abajo 👇'
            )
        },
        "movie_info": {
            "seasons": "Temporadas:",
            "current_season": "Temporada actual",
            "number_of_episodes": "Número de episodios:",
            "episodes": "Episodios:",
            "last_episode": "Último episodio:",
            "next_episod_date": "Próximo episodio:",
            "genre": "Género:",
            "release": "📅 Estreno:",
            "rating": "⭐ Valoración:",
            "already_added": "ya está en tu biblioteca",
        },
        "next_episode_info": {
            "title": "Título",
            "season_number": "Temporada",
            "episode_number": "Episodio",
        },
    },
    # turkish
    'tr': {
        'button': {
           'providers': 'Sağlayıcılar',
            'remove': 'Kaldır',
            "remove_from": "Kitaplıktan kaldır",
            "add": "Kitaplığa ekle",
            'details': 'Detaylar',
            'languages': 'Diller',
            'trailer': 'Fragman',
            'find_movie': 'Film bul',
            'find_tv': 'Dizi bul',
            'subscribe': 'Abone ol'
        },
        'message': {
            'not_found': 'Bulunamadı',
            'no_descriptions': 'Açıklama yok',
            'no_information_available': 'Bilgi mevcut değil'
        },
        'stop': {
            'first': 'Bunu bir daha yapma.',
            'second': '❌ DUR!',
            'third': '❌ DUUUR !!!',
            'last': 'Lütfen, dur. Lütfen...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Sağlayıcılar:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Mevcut diller:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Yeni bölüm yayınlandı.",
            "movie": lambda title: f"❗ <b>{title}</b> bugün yayınlandı!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Fragman: {trailer_url}',
            'not_awailable': 'Fragman mevcut değil'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> kütüphanene eklendi",
            'already_added': lambda title: f"✅ <b>{title}</b> zaten kütüphanende var",
        },
        "follow_list": {
            "title": "🎬 <b><i>Kütüphaneniz:</i></b> \n",
            "not_found_in_list": "❌ Hata. Film kütüphanenizde bulunamadı.",
            "empty_list": "<b><i>Kütüphaneniz boş.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> kütüphanenizden kaldırıldı",
            "already_removed": "Bu filmi zaten kaldırdınız",
        },
        'payment': {
            'title': 'Ödeme sistemini seçin:',
            'session_completed': '✅ Ödemeniz işleniyor. Biraz zaman alabilir.',
            'payment_succeeded': '✅ Ödeme başarılı, abonelik aktif!',
            'payment_failed': '⚠️ Abonelik ödemeniz başarısız oldu. Kartınızı kontrol edin.',
            'stop': '✅ Aboneliğiniz, ödenmiş dönem sonunda iptal edilecektir.',
            'fail_stop': '❌ Abonelik iptali başarısız oldu. Lütfen daha sonra tekrar deneyin.',
            'subscription_deleted': '❌ Aboneliğiniz artık aktif değil.',
            'not_found': '⚠️ Aktif aboneliğiniz yok',
            'subscription_expired': (
                '❌ <b>Aboneliğinizin süresi doldu.</b>\n'
                'Yeni bildirimler almak istiyorsanız, lütfen aşağıdaki butona tıklayın 👇'
            )
        },
        "movie_info": {
            "seasons": "Sezonlar:",
            "current_season": "Geçerli sezon",
            "number_of_episodes": "Bölüm sayısı:",
            "episodes": "Bölümler:",
            "last_episode": "Son bölüm:",
            "next_episod_date": "Sonraki bölüm:",
            "genre": "Tür:",
            "release": "📅 Yayın tarihi:",
            "rating": "⭐ Puan:",
            "already_added": "zaten kitaplığında var",
        },
        "next_episode_info": {
            "title": "Başlık",
            "season_number": "Sezon",
            "episode_number": "Bölüm",
        },
    },
    # czech
    'cs': {
        'button': {
           'providers': 'Poskytovatelé',
            'remove': 'Odstranit',
            "remove_from": "Odebrat z knihovny",
            "add": "Přidat do knihovny",
            'details': 'Detaily',
            'languages': 'Jazyky',
            'trailer': 'Upoutávka',
            'find_movie': 'Najít film',
            'find_tv': 'Najít seriál',
            'subscribe': 'Odebírat'
        },
        'message': {
            'not_found': 'Nenalezeno',
            'no_descriptions': 'Žádné popisy',
            'no_information_available': 'Žádné dostupné informace'
        },
        'stop': {
            'first': 'Nepokoušej se to znovu.',
            'second': '❌ ZASTAV TO.',
            'third': '❌ ZAS-TAV TO !!!',
            'last': 'Prosím, zastav to. Prosím...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Poskytovatelé:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Dostupné jazyky:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nová epizoda byla vydána.",
            "movie": lambda title: f"❗ <b>{title}</b> vyšla dnes!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Upoutávka: {trailer_url}',
            'not_awailable': 'Upoutávka není k dispozici'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> bylo přidáno do vaší knihovnyu",
            'already_added': lambda title: f"✅ <b>{title}</b> již je ve vaší knihovně",
        },
        "follow_list": {
            "title": "🎬 <b><i>Vaše knihovna:</i></b> \n",
            "not_found_in_list": "❌ Chyba. Film nebyl nalezen ve vaší knihovně.",
            "empty_list": "<b><i>Vaše knihovna je prázdná.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> byl odstraněn z vaší knihovny",
            "already_removed": "Tento film jste již odstranili",
        },
        'payment': {
            'title': 'Vyberte platební systém:',
            'session_completed': '✅ Zpracováváme vaši platbu. Může to chvíli trvat.',
            'payment_succeeded': '✅ Platba byla úspěšná, předplatné aktivováno!',
            'payment_failed': '⚠️ Platba vašeho předplatného selhala. Zkontrolujte svou kartu.',
            'stop': '✅ Vaše předplatné bude zrušeno po skončení zaplaceného období.',
            'fail_stop': '❌ Zrušení předplatného se nezdařilo. Zkuste to prosím později.',
            'subscription_deleted': '❌ Vaše předplatné již není aktivní.',
            'not_found': '⚠️ Nemáte žádné aktivní předplatné',
            'subscription_expired': (
                '❌ <b>Vaše předplatné vypršelo.</b>\n'
                'Pokud chcete dostávat nové oznámení, klikněte na tlačítko níže 👇'
            )
        },
        "movie_info": {
            "seasons": "Sezóny:",
            "current_season": "Aktuální sezóna",
            "number_of_episodes": "Počet epizod:",
            "episodes": "Epizody:",
            "last_episode": "Poslední epizoda:",
            "next_episod_date": "Další epizoda:",
            "genre": "Žánr:",
            "release": "📅 Datum vydání:",
            "rating": "⭐ Hodnocení:",
            "already_added": "už je ve vaší knihovně",
        },
        "next_episode_info": {
            "title": "Název",
            "season_number": "Sezóna",
            "episode_number": "Epizoda",
        },
    },
    # nederlands
    'nl': {
        'button': {
           'providers': 'Providers',
            'remove': 'Verwijderen',
            "remove_from": "Verwijderen uit bibliotheek",
            "add": "Toevoegen aan bibliotheek",
            'details': 'Details',
            'languages': 'Talen',
            'trailer': 'Trailer',
            'find_movie': 'Vind een film',
            'find_tv': 'Vind een tv-serie',
            'subscribe': 'Abonneren'
        },
        'message': {
            'not_found': 'Niet gevonden',
            'no_descriptions': 'Geen beschrijvingen',
            'no_information_available': 'Geen beschikbare informatie'
        },
        'stop': {
            'first': 'Doe dat niet nog eens.',
            'second': '❌ STOP HIERMEE.',
            'third': '❌ STO-OP !!!',
            'last': 'Alsjeblieft, stop. Alsjeblieft...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Providers:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Beschikbare talen:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nieuwe aflevering uitgebracht.",
            "movie": lambda title: f"❗ <b>{title}</b> is vandaag uitgebracht!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
            'not_awailable': 'Trailer niet beschikbaar'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> is toegevoegd aan je bibliotheek",
            'already_added': lambda title: f"✅ <b>{title}</b> staat al in je bibliotheek",
        },
        "follow_list": {
            "title": "🎬 <b><i>Je bibliotheek:</i></b> \n",
            "not_found_in_list": "❌ Fout. Film niet gevonden in je bibliotheek.",
            "empty_list": "<b><i>Je bibliotheek is leeg.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> is verwijderd uit je bibliotheek",
            "already_removed": "Je hebt deze film al verwijderd",
        },
        'payment': {
            'title': 'Selecteer het betalingssysteem:',
            'session_completed': '✅ We verwerken je betaling. Dit kan even duren.',
            'payment_succeeded': '✅ Betaling succesvol, abonnement geactiveerd!',
            'payment_failed': '⚠️ Je abonnementsbetaling is mislukt. Controleer je kaart.',
            'stop': '✅ Je abonnement wordt beëindigd aan het einde van de betaalde periode.',
            'fail_stop': '❌ Abonnement annuleren is mislukt. Probeer het later opnieuw.',
            'subscription_deleted': '❌ Je abonnement is niet meer actief.',
            'not_found': '⚠️ Je hebt geen actieve abonnementen',
            'subscription_expired': (
                '❌ <b>Je abonnement is verlopen.</b>\n'
                'Als je nieuwe meldingen wilt ontvangen, klik dan op de knop hieronder 👇'
            )
        },
        "movie_info": {
            "seasons": "Seizoenen:",
            "current_season": "Huidig seizoen",
            "number_of_episodes": "Aantal afleveringen:",
            "episodes": "Afleveringen:",
            "last_episode": "Laatste aflevering:",
            "next_episod_date": "Volgende aflevering:",
            "genre": "Genre:",
            "release": "📅 Releasedatum:",
            "rating": "⭐ Beoordeling:",
            "already_added": "staat al in je bibliotheek",
        },
        "next_episode_info": {
            "title": "Titel",
            "season_number": "Seizoen",
            "episode_number": "Aflevering",
        },

    },
    # hungarian
    'hu': {
        'button': {
           'providers': 'Szolgáltatók',
            'remove': 'Eltávolítás',
            "remove_from": "Eltávolítás a könyvtárból",
            "add": "Hozzáadás a könyvtárhoz",
            'details': 'Részletek',
            'languages': 'Nyelvek',
            'trailer': 'Előzetes',
            'find_movie': 'Film keresése',
            'find_tv': 'Sorozat keresése',
            'subscribe': 'Feliratkozás'
        },
        'message': {
            'not_found': 'Nem található',
            'no_descriptions': 'Nincs leírás',
            'no_information_available': 'Nincs elérhető információ'
        },
        'stop': {
            'first': 'Ne tedd újra.',
            'second': '❌ ÁLLJ MEG!',
            'third': '❌ ÁLLJAA!!!',
            'last': 'Kérlek, állj meg. Kérlek...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Szolgáltatók:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Elérhető nyelvek:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Új epizód jelent meg.",
            "movie": lambda title: f"❗ <b>{title}</b> ma jelent meg!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Előzetes: {trailer_url}',
            'not_awailable': 'Előzetes nem elérhető'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> hozzáadva a könyvtáradhoz",
            'already_added': lambda title: f"✅ <b>{title}</b> már a könyvtáradban van",
        },
        "follow_list": {
            "title": "🎬 <b><i>Könyvtárad:</i></b> \n",
            "not_found_in_list": "❌ Hiba. A film nem található a könyvtáradban.",
            "empty_list": "<b><i>A könyvtárad üres.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> eltávolítva a könyvtáradból",
            "already_removed": "Ezt a filmet már eltávolítottad",
        },
        'payment': {
            'title': 'Válassza ki a fizetési rendszert:',
            'session_completed': '✅ Feldolgozzuk a fizetésed. Ez eltarthat egy ideig.',
            'payment_succeeded': '✅ Sikeres fizetés, előfizetés aktiválva!',
            'payment_failed': '⚠️ Az előfizetés fizetése sikertelen. Ellenőrizd a kártyádat.',
            'stop': '✅ Az előfizetés a fizetett időszak végén le lesz mondva.',
            'fail_stop': '❌ Az előfizetés lemondása sikertelen. Kérlek próbáld újra később.',
            'subscription_deleted': '❌ Az előfizetésed már nem aktív.',
            'not_found': '⚠️ Nincs aktív előfizetésed',
            'subscription_expired': (
                '❌ <b>Az előfizetésed lejárt.</b>\n'
                'Ha új értesítéseket szeretnél kapni, kattints az alábbi gombra 👇'
            )
        },
        "movie_info": {
            "seasons": "Évadok:",
            "current_season": "Jelenlegi évad",
            "number_of_episodes": "Epizódok száma:",
            "episodes": "Epizódok:",
            "last_episode": "Utolsó epizód:",
            "next_episod_date": "Következő epizód:",
            "genre": "Műfaj:",
            "release": "📅 Megjelenés:",
            "rating": "⭐ Értékelés:",
            "already_added": "már a könyvtáradban van",
        },
        "next_episode_info": {
            "title": "Cím",
            "season_number": "Évad",
            "episode_number": "Epizód",
        },

    },
    # Norwegian
    'nb': {
        'button': {
           'providers': 'Leverandører',
            'remove': 'Fjern',
            "remove_from": "Fjern fra biblioteket",
            "add": "Legg til i biblioteket",
            'details': 'Detaljer',
            'languages': 'Språk',
            'trailer': 'Trailer',
            'find_movie': 'Finn en film',
            'find_tv': 'Finn en TV-serie',
            'subscribe': 'Abonner'
        },
        'message': {
            'not_found': 'Ikke funnet',
            'no_descriptions': 'Ingen beskrivelser',
            'no_information_available': 'Ingen informasjon tilgjengelig'
        },
        'stop': {
            'first': 'Ikke gjør det igjen.',
            'second': '❌ STOPP!',
            'third': '❌ STO-O-PP!!!',
            'last': 'Vær så snill, stopp. Vær så snill...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Leverandører:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Tilgjengelige språk:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Ny episode utgitt.",
            "movie": lambda title: f"❗ <b>{title}</b> ble utgitt i dag!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
            'not_awailable': 'Ingen trailer tilgjengelig'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> ble lagt til i biblioteket ditt",
            'already_added': lambda title: f"✅ <b>{title}</b> finnes allerede i biblioteket ditt",
        },
        "follow_list": {
            "title": "🎬 <b><i>Ditt bibliotek:</i></b> \n",
            "not_found_in_list": "❌ Feil. Filmen ble ikke funnet i biblioteket ditt.",
            "empty_list": "<b><i>Ditt bibliotek er tomt.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> er fjernet fra biblioteket ditt",
            "already_removed": "Du har allerede fjernet denne filmen",
        },
        'payment': {
            'title': 'Velg betalingssystem:',
            'session_completed': '✅ Vi behandler betalingen din. Dette kan ta litt tid.',
            'payment_succeeded': '✅ Betaling vellykket, abonnement aktivert!',
            'payment_failed': '⚠️ Abonnementsbetalingen mislyktes. Vennligst sjekk kortet ditt.',
            'stop': '✅ Abonnementet ditt avsluttes ved slutten av den betalte perioden.',
            'fail_stop': '❌ Kunne ikke kansellere abonnementet. Prøv igjen senere.',
            'subscription_deleted': '❌ Abonnementet ditt er ikke lenger aktivt.',
            'not_found': '⚠️ Du har ingen aktive abonnementer',
            'subscription_expired': (
                '❌ <b>Abonnementet ditt har utløpt.</b>\n'
                'Hvis du vil motta nye varsler, vennligst klikk på knappen nedenfor 👇'
            )
        },
        "movie_info": {
            "seasons": "Sesonger:",
            "current_season": "Nåværende sesong",
            "number_of_episodes": "Antall episoder:",
            "episodes": "Episoder:",
            "last_episode": "Siste episode:",
            "next_episod_date": "Neste episode:",
            "genre": "Sjanger:",
            "release": "📅 Utgivelse:",
            "rating": "⭐ Vurdering:",
            "already_added": "allerede i biblioteket ditt",
        },
        "next_episode_info": {
            "title": "Tittel",
            "season_number": "Sesong",
            "episode_number": "Episode",
        },
    },
    # swedish
    'sv': {
        'button': {
           'providers': 'Leverantörer',
            'remove': 'Ta bort',
            "remove_from": "Ta bort från biblioteket",
            "add": "Lägg till i biblioteket",
            'details': 'Detaljer',
            'languages': 'Språk',
            'trailer': 'Trailer',
            'find_movie': 'Hitta en film',
            'find_tv': 'Hitta en TV-serie',
            'subscribe': 'Prenumerera'
        },
        'message': {
            'not_found': 'Inte hittad',
            'no_descriptions': 'Inga beskrivningar',
            'no_information_available': 'Ingen information tillgänglig'
        },
        'stop': {
            'first': 'Gör inte det igen.',
            'second': '❌ SLUTA!',
            'third': '❌ SLU-U-UTA!!!',
            'last': 'Snälla, sluta. Snälla...'
        },
        'providers': lambda title, text: f'<b>{title}</b>\n<u>Leverantörer:</u>\n\n{text}',
        'languages': lambda langs_text: f'🎬 <b>Tillgängliga språk:</b>\n\n{langs_text}',
        "release": {
            "new_episod": "❗ Nytt avsnitt släppt.",
            "movie": lambda title: f"❗ <b>{title}</b> släpptes idag!"
        },
        'trailer': {
            'show_trailer': lambda trailer_url: f'🎬 Trailer: {trailer_url}',
            'not_awailable': 'Ingen trailer tillgänglig'
        },
        'add_movie': {
            'add': lambda title: f"✅ <b>{title}</b> har lagts till i ditt bibliotek",
            'already_added': lambda title: f"✅ <b>{title}</b> finns redan i ditt bibliotek",
        },
        "follow_list": {
            "title": "🎬 <b><i>Ditt bibliotek:</i></b> \n",
            "not_found_in_list": "❌ Fel. Filmen hittades inte i ditt bibliotek.",
            "empty_list": "<b><i>Ditt bibliotek är tomt.</i></b>",
            "remove": lambda movie_title: f"<b>{movie_title}</b> har tagits bort från ditt bibliotek",
            "already_removed": "Du har redan tagit bort denna filmen",
        },
        'payment': {
            'title': 'Välj betalningssystem:',
            'session_completed': '✅ Vi behandlar din betalning. Det kan ta lite tid.',
            'payment_succeeded': '✅ Betalningen lyckades, prenumerationen är aktiverad!',
            'payment_failed': '⚠️ Din betalning för prenumerationen misslyckades. Kontrollera ditt kort.',
            'stop': '✅ Din prenumeration kommer att avslutas i slutet av den betalda perioden.',
            'fail_stop': '❌ Det gick inte att avsluta prenumerationen. Försök igen senare.',
            'subscription_deleted': '❌ Din prenumeration är inte längre aktiv.',
            'not_found': '⚠️ Du har inga aktiva prenumerationer',
            'subscription_expired': (
                '❌ <b>Din prenumeration har gått ut.</b>\n'
                'Om du vill få nya aviseringar, klicka på knappen nedan 👇'
            )
        },
        "movie_info": {
            "seasons": "Säsonger:",
            "current_season": "Nuvarande säsong",
            "number_of_episodes": "Antal avsnitt:",
            "episodes": "Avsnitt:",
            "last_episode": "Sista avsnittet:",
            "next_episod_date": "Nästa avsnitt:",
            "genre": "Genre:",
            "release": "📅 Utgivning:",
            "rating": "⭐ Betyg:",
            "already_added": "redan i ditt bibliotek",
        },
        "next_episode_info": {
            "title": "Titel",
            "season_number": "Säsong",
            "episode_number": "Avsnitt",
        },
    }

}
