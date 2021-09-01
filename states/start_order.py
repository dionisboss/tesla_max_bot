from aiogram.dispatcher.filters.state import StatesGroup, State


class Order_state(StatesGroup):
    Chose_Gender = State()
    Chose_Age = State()
    Chose_Body_Type = State()
    Budget = State()
    Date_Time = State()
    Location = State()
    Chose_preferences = State()
    Contact_info = State()
    User_Confirmation = State()

