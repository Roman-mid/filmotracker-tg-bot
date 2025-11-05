from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BOT_KEY = os.getenv("BOT_KEY")
MASTER_ID = int(os.getenv("MASTER_ID", "0"))
DATABASE_URL = os.getenv("DATABASE_URL")
PAYMENT_KEY = os.getenv("PAYMENT_KEY")
SMART_GLOCAL_API = os.getenv("SMART_GLOCAL_API")
STRIPE_PROD_ID = os.getenv("STRIPE_PROD_ID")
STRIPE_PRICE_ID = os.getenv("STRIPE_PRICE_ID")
STRIPE_APY_KEY = os.getenv("STRIPE_APY_KEY")
STRIPE_WEBHOOK = os.getenv("STRIPE_WEBHOOK")
MOVIE_API_URL = os.getenv("MOVIE_API_URL")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")