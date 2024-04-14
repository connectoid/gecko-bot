from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon_en import UNRECOGNIZED_COMMAND
from lexicon.lexicon import BUTTON, MESSAGE

router: Router = Router()


@router.message()
async def send_echo(message: Message):
    lang = 'ru'
    await message.answer(MESSAGE[lang]['UNRECOGNIZED_COMMAND'])


