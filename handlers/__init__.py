from .start import register_start_handlers
from .catalog import register_catalog_handlers
from .offer import register_offer_handlers
from .cart import register_cart_handlers


def register_all_handlers(dp):
    register_start_handlers(dp)
    register_catalog_handlers(dp)
    register_offer_handlers(dp)
    register_cart_handlers(dp)


    # To answer empty callback quieries(always last registered!!!)
    dp.callback_query.register(
        answer_callback
    )


async def answer_callback(callback_query):
    await callback_query.answer()
