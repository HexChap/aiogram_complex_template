import asyncio

from dataclasses import dataclass

from aiogram import Bot, Dispatcher
from aiogram.types.message import ParseMode
from aiogram.contrib.fsm_storage.files import JSONStorage


@dataclass
class Database:
    address = "DATABASE IP ADDRESS"
    port = 5432
    db_name = "DATABASE NAME"
    user = "USERNAME"
    password = "USER's PASSWORD"


@dataclass
class Settings:
    token = "YOUR_TOKEN"
    owner_id = 1370280956
    database = Database


bot = Bot(token=Settings.token, parse_mode=ParseMode.MARKDOWN)
storage = JSONStorage(r"data\states.json")
dispatcher = Dispatcher(bot, storage=storage)

