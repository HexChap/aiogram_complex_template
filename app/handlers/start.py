from gettext import gettext as _

from aiogram import types
from aiogram.dispatcher import FSMContext

from app.core.settings import dispatcher as dp
from app.core.states import HelloState


@dp.message_handler(state="*", commands=["start"])
async def start(msg: types.Message):
    await HelloState.name.set()

    await msg.reply(_("What's your name?"))


@dp.message_handler(state=HelloState.name)
async def process_start(msg, state: FSMContext):
    await msg.reply(
        _("Welcome, {text}!").format(text=msg.text)
    )
