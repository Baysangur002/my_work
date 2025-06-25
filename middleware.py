from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Dict, Awaitable, Callable
from aiogram import types
from aiogram.enums import ChatAction  # enum с типами действий «typing», «upload_photo» …


class SimpleMLoggerMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        print(f'Произошел update: {event} ')
        return await handler(event, data)


class TypingActionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.TelegramObject, data: dict):
        # Работает только на входящих сообщениях
        if isinstance(event, types.Message):
            # ► Telegram отображает индикатор ~5 сек.; если хендлер дольше — можно повторить
            await event.answer_chat_action(ChatAction.TYPING)

        return await handler(event, data)  # не забываем продолжить цепочку