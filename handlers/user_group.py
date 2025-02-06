from aiogram import F, types, Router
from string import punctuation
from filters.chat_types import ChatTypeFilter
from aiogram.filters import CommandStart

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_group_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Денис, пуш!")

bad_habits = {
    'курить', 'курил', 'покурю', 'покурил'
}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if bad_habits.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.username}, курить он пошёл, ну ну...")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
