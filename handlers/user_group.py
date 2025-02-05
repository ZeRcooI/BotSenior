from string import punctuation

from aiogram import F, types, Router

user_group_router = Router()

restricted_words = {
    'пизда', 'ебать', 'сука', 'нахуй', 'долбоеб', 'чмо', 'тварь', 'гондон', 'пиздец',
    'заебал', 'гандон', 'еблан', 'курва', 'хер', 'срань', 'уебок', 'пидор', 'дрочить',
    'ссать', 'гавно', 'сучка', 'педик', 'мудило', 'ублюдок', 'ебанат', 'гнида', 'пиздюк',
    'шлюха', 'манда', 'ебанутый', 'похоть', 'ебучий', 'пипец', 'член', 'хуяк', 'тупица',
    'пизды', 'бля', 'урод', 'шмара', 'блять', 'задрот', 'падла'
}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f"{message.from_user.username}, дурной чтоль, ты че ругаешься?!")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
