from aiogram import types, Dispatcher
from aiogram.filters import StateFilter, CommandStart

from markups.main import main_inline_markup


async def start_cmd(m: types.Message):
    await m.answer(
        "Добро пожаловать!",
        reply_markup=main_inline_markup
    )


def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_cmd, CommandStart())
