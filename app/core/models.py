from tortoise import Model
from tortoise.fields import IntField, DatetimeField


class AbstractModel(Model):
    id = IntField(pk=True, unique=True)
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        abstract = True
