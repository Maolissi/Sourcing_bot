from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    items = [
        ("Vacancies", "vacancies"),
        ("New Search", "new_search"),
        ("Candidates", "candidates"),
        ("Daily Reports", "reports"),
        ("Outreach", "outreach"),
        ("Settings", "settings"),
    ]
    for label, callback_data in items:
        builder.button(text=label, callback_data=f"menu:{callback_data}")
    builder.adjust(2, 2, 2)
    return builder.as_markup()
