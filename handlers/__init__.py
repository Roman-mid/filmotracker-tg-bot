from .start import router as start_router
from .search import router as search_router
from .details import router as details_router
from .trailer import router as trailer_router
from .languages import router as languages_router
from .add_movie import router as add_movie_router
from .show_follow_list import router as show_follow_list_router
from .remove_movie_from_list import router as remove_movie_from_list_router
from .remove_movie import router as remove_movie_router
from .not_text import router as not_text_message_router
from .process_pre_checkout import router as process_pre_checkout_router
from .send_subscription_invoice import router as send_subscription_invoice_router
from payment.stripe.stripe import router as stripe_create_checkout_session_router
# from .stop_stripe_subscription import router as unsubscribe_user_router
from .show_lang_settings import router as show_lang_settings_router
from .select_user_lang import router as select_user_lang_router
from .help import router as help_router

routers = [
    start_router,
    show_follow_list_router,
    show_lang_settings_router,
    select_user_lang_router,
    help_router,
    search_router,
    details_router,
    trailer_router,
    languages_router,
    add_movie_router,
    remove_movie_router,
    remove_movie_from_list_router,
    not_text_message_router,
    process_pre_checkout_router,
    send_subscription_invoice_router,
    stripe_create_checkout_session_router,
    # unsubscribe_user_router
]
