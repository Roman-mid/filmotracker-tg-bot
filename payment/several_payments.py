    # to have several payment methods
    # subscribe_btn = InlineKeyboardButton(
    #   text=content['button']['subscribe'],
    #   callback_data=FindCallback(
    #     action="subscribe"
    #   ).pack(),
    # )

    # kb = InlineKeyboardMarkup(inline_keyboard=[
    #   [subscribe_btn]
    # ])
    # await bot.send_message( 
    #   user_id, 
    #   subscription_expired, 
    #   parse_mode="HTML", 
    #   reply_markup=kb
    # )