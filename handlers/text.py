from idlelib.autocomplete_w import AutoCompleteWindow

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from filters import ContainWorld

router = Router()

@router.message(ContainWorld('бомба'))
async def cmd_bad(message: Message, bot: Bot):
    await bot.send_message(5244157750, f'@{message.from_user.username} употребляет список запрещенных фраз')

