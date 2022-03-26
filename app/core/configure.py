from tortoise import Tortoise

from .settings import Settings


db = Settings.database
DB_URL = (
    "postgres://"
    f"{db.user}:{db.password}@"
    f"{db.address}:{db.port}/{db.db_name}"
)


async def configure_db():
    await Tortoise.init(db_url=DB_URL, modules={"models": ["app.core.models"]})
    await Tortoise.generate_schemas()
