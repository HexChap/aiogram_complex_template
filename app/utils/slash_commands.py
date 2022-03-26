from gettext import gettext as _

from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    await bot.delete_my_commands()

    commands = [
        BotCommand(command="/start", description=_("Start command")),
    ]

    await bot.set_my_commands(commands)
