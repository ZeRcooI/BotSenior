from aiogram.types import BotCommand

private = [
    BotCommand(command='admin', description="Доступно только для администратора"),
    BotCommand(command='start', description='Старт'),
    BotCommand(command='menu', description="Посмотреть меню"),
    BotCommand(command='about', description="Про бота"),
    BotCommand(command='payment', description="Варианты оплаты"),
    BotCommand(command='shipping', description="Варианты доставки")
]
