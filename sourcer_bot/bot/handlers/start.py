from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from sourcer_bot.bot.keyboards.main_menu import main_menu_keyboard

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "<b>Welcome to your Sourcer Workspace!</b>\\n\\n"
        "Manage vacancies, run sourcing searches, review candidates, "
        "prepare outreach drafts, and track daily results.",
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        "<b>How to use Sourcer Bot</b>\\n"
        "Choose an action from the menu. Searches are started manually, "
        "and outreach messages are drafts for your review."
    )
