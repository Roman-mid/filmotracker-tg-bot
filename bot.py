# import asyncio
# from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.memory import MemoryStorage
# from config import BOT_KEY
# from handlers import routers
# from middlewares.subscription import SubscriptionMiddleware
# from services.scheduler import scheduler
# from models import init_db

# bot = Bot(BOT_KEY)
# dp = Dispatcher(storage=MemoryStorage())

# dp.message.middleware(SubscriptionMiddleware())
# dp.callback_query.middleware(SubscriptionMiddleware())

# for r in routers:
#     dp.include_router(r)

# async def start_bot():
#     asyncio.create_task(scheduler(bot))
#     await dp.start_polling(bot)

# async def main():
#     await init_db()
#     await start_bot()

# if __name__ == "__main__":
#     asyncio.run(main())






















import asyncio
from aiohttp import web
from config import BOT_KEY, PORT
from handlers import routers
from services.tmdb_client import client
from middlewares.subscription import SubscriptionMiddleware
from models import init_db
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from services.scheduler import scheduler
from payment.stripe.stripe_webhook import stripe_webhook


bot = Bot(BOT_KEY)
dp = Dispatcher(storage=MemoryStorage())

dp.message.middleware(SubscriptionMiddleware())
dp.callback_query.middleware(SubscriptionMiddleware())

for r in routers:
    dp.include_router(r)

async def start_bot():
    asyncio.create_task(scheduler(bot))
    await dp.start_polling(bot)

async def start_webhook_server():
    app = web.Application()

    # Stripe webhook
    app.router.add_post("/stripe/webhook", stripe_webhook)

    # static files (CSS, JS, HTML)
    app.router.add_static('/static/', path='static', name='static')

    # ✅ routes for success и cancel pages
    app.router.add_get("/success", lambda request: web.FileResponse("static/success.html"))
    app.router.add_get("/cancel", lambda request: web.FileResponse("static/cancel.html"))

    # execute
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"🌍 Stripe webhook server started at http://0.0.0.0:{PORT}")



async def main():
    await init_db()

    # run the bot and webhook
    await asyncio.gather(
        start_bot(),
        start_webhook_server(),
    )

if __name__ == "__main__":
    asyncio.run(main())

