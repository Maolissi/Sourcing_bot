from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router(name="callbacks")

SECTIONS = {
    "vacancies": "Vacancies",
    "new_search": "New Search",
    "candidates": "Candidates",
    "reports": "Daily Reports",
    "outreach": "Outreach Drafts",
    "settings": "Settings",
}


@router.callback_query(F.data.startswith("menu:"))
async def menu_callback(callback: CallbackQuery) -> None:
    section = callback.data.removeprefix("menu:")
    title = SECTIONS.get(section)
    if title is None:
        await callback.answer("Unknown menu action.", show_alert=True)
        return

    await callback.answer()
    if callback.message:
        await callback.message.answer(
            f"<b>{title}</b>\\n\\nThis module is planned for the next implementation steps."
        )
