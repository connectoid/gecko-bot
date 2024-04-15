from time import sleep
from datetime import datetime

from aiogram import Bot, Dispatcher, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove, LabeledPrice
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage

from lexicon.lexicon_en import (LEXICON_HELP, START_MESSAGE,
                                FEEDBACK_TEXT, FEEDBACK_SENT, MAIN_MENU_BUTTON, HELP_BUTTON, HISTORY_BUTTON,
                                TO_MAIN_MENU_BUTTON, REMAINS_BUTTON, REPEAT_BUTTON, PROFILE_BUTTON,
                                TARIFF_BUTTON)
from lexicon.lexicon import MESSAGE, BUTTON, TARIFF, BROADCAST
from keyboards.commands_menu import set_commands_menu
from config_data.config import Config, load_config
from utils.utils import send_to_admin
from filters.user_type import IsAdminFilter
from services.requests_insta import get_video_url

storage = MemoryStorage()
router = Router()
config: Config = load_config()


lang = 'ru'
switch_reporting = True

# config: Config = load_config()
# bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

@router.message(F.text.contains('instagram.com/reel/'))
async def content_type_example(message: Message):
    time_start = datetime.now()
    url = message.text
    video_url = get_video_url(url)
    time_end = datetime.now()
    if video_url:
        print('Ссылка на видео полуена в Хэндлере')
        # await bot.send_video(message.chat.id, video_url)
        await message.answer(text=f'Время на получение ссылки на видео: {time_end - time_start}')
    else:
        print('Ссылка на видео НЕ полуена в Хэндлере')
        await message.answer(text='Ошибка получения ссылки на видео (см. логи)')


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, bot: Bot):
    fname = message.from_user.first_name
    lname = message.from_user.last_name
    tg_id = message.from_user.id
    await message.answer(
        text=MESSAGE[lang]['START_MESSAGE'])

