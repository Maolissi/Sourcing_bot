from sourcer_bot.bot.keyboards.main_menu import main_menu_keyboard


def test_main_menu_has_six_buttons() -> None:
    keyboard = main_menu_keyboard()
    assert len(keyboard.inline_keyboard) == 3
    assert sum(len(row) for row in keyboard.inline_keyboard) == 6
