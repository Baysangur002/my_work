from tkinter.messagebox import RETRY

from aiogram.filters import BaseFilter
from aiogram.types import Message
from config import ADMIN

class AdminFilters(BaseFilter):
    async def __call__(self, message: Message):
        if message.from_user.id in ADMIN:
            return True
        return False


class ContainWorld(BaseFilter):
    def __init__(self, text):
        self.text = text.lower()

    async def __call__(self, message: Message):
        if self.text in message.text.lower():
            return True
        return False

    git
    add
    README.md
    git
    commit - m
    "первый коммит"
    git
    branch - M
    main
    git
    remote
    add
    origin
    https: // github.com / Baysangur002 / my_work.git
    git
    push - u
    origin
    main



