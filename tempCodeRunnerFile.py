async def start_webhook_server():
    app = web.Application()
    app.router.add_post("/stripe/webhook", stripe_webhook)
    app.router.add_static('/static/', path='static', name='static')
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()
    print("🌍 Stripe webhook server started at http://0.0.0.0:8000")