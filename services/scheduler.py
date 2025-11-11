import asyncio
from handlers.check_follow_list import check_follow_list
from handlers.tools.user.get_all_active_users import get_all_users

# CHECK_INTERVAL = 10
CHECK_INTERVAL = 7200
# CHECK_INTERVAL = 24 * 60 * 60  # a day

async def scheduler(bot):
  while True:
    try:
      users = await get_all_users()
      if not users:
        print("[Scheduler] No active users found")
      else:
        tasks = [check_follow_list(bot, u) for u in users]
        await asyncio.gather(*tasks, return_exceptions=True)
    except Exception as e:
      print(f"[Scheduler error] {e}")

    await asyncio.sleep(CHECK_INTERVAL)
