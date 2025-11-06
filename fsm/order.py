from aiogram.fsm.state import State, StatesGroup


class CreateOrderFSM(StatesGroup):
    name_state = State()
    phone_number_state = State()
