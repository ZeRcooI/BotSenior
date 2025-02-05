from aiogram import F, types, Router
from string import punctuation
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {
    'пизда', 'ебать', 'сука', 'нахуй', 'долбоеб', 'чмо', 'тварь', 'гондон', 'пиздец',
    'заебал', 'гандон', 'еблан', 'курва', 'нахуя', 'заебать', 'уебок', 'пидор', 'заебете',
    'пизду', 'говно', 'сучка', 'ахуели', 'уёбок', 'ублюдок', 'ебанат', 'заебёте', 'пиздюк',
    'шлюха', 'гавно', 'ебанутый', 'хуя', 'ебучий', 'ахуеть', 'ахуела', 'хуяк', 'шлюхи',
    'пизды', 'бля', 'ебаное', 'ахуела', 'блять', 'пидорасина', 'пидорас'
}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.username}, дурной чтоль, ты чё ругаешься?!")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
