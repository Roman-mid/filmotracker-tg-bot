from aiogram import Router, types, F

router = Router()

@router.pre_checkout_query()
async def process_pre_checkout(pre_checkout: types.PreCheckoutQuery):
    await pre_checkout.answer(ok=True)
