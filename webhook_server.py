import asyncio
from aiohttp import web
from config import PORT
from payment.stripe.stripe_webhook import stripe_webhook

async def start_webhook_server():
  app = web.Application()

  app.router.add_post("/stripe/webhook", stripe_webhook)
  app.router.add_static('/static/', path='static', name='static')
  app.router.add_get("/success", lambda request: web.FileResponse("static/success.html"))
  app.router.add_get("/cancel", lambda request: web.FileResponse("static/cancel.html"))

  runner = web.AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, "0.0.0.0", PORT)
  await site.start()
  print(f"🌍 Stripe webhook server started at http://0.0.0.0:{PORT}")

  while True:
    await asyncio.sleep(3600)

if __name__ == "__main__":
  asyncio.run(start_webhook_server())
