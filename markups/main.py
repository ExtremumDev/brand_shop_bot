from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_inline_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛍 Открыть список брендов",
                callback_data="catalog"
            )
        ],
        [
            InlineKeyboardButton(
                text="🛒 Открыть мою корзину",
                callback_data="open_cart"
            )
        ]
    ]
)
