import aiogram

import app.handlers
from app.core.settings import bot, dispatcher
from app.core.configure import configure_db
from app.utils import set_commands


async def on_startup(dp: aiogram.Dispatcher):
    await configure_db()

    await set_commands(bot)


if __name__ == '__main__':
    aiogram.executor.start_polling(dispatcher, on_startup=on_startup)
