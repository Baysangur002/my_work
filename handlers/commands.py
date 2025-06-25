from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext



router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Марша вог1ийла')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('По любым техническим вопросам: @b_terloev')


@router.message(Command('admin'))
async def cmd_admin(message: Message):
    await message.answer('Привет Сэр')