from aiogram import Router
from .commands import router as command_router
from .text import router as text_router
router = Router()

router.include_routers(command_router, text_router)