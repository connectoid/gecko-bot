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
from keyboards.inline_keyboards import create_bottom_keyboard
from config_data.config import Config, load_config
from utils.utils import send_to_admin
from filters.user_type import IsAdminFilter
from services.requests_insta import get_video_requests
from services.instagrapi_insta import get_video_instagrapi
from services.selenium_insta import get_video_selenium

storage = MemoryStorage()
router = Router()
config: Config = load_config()

lang = 'ru'
switch_reporting = True

methods_buttons = [
    'selenium',
    'requests',
    'instagrapi',
    'instaload',
    'hikerAPI'
]

config: Config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

@router.message(F.text.contains('instagram.com/reel/'))
async def content_type_example(message: Message):
    url = message.text
    print(url)
    shortcode = url.split('/reel/')[1].split('/')[0]
    await message.answer(text='Выберите метод получения ссылки на видео',
                         reply_markup=create_bottom_keyboard(methods_buttons, shortcode))
    

@router.callback_query(Text(startswith='selenium'))
async def process_requests_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    shortcode = callback.data.split(' ')[-1]
    print(shortcode)
    video_url = get_video_selenium(shortcode)
    if video_url:
        video_url = video_url[:50]
        time_end = datetime.now()
        print(video_url)
        print('Ссылка на видео полуена в Хэндлере')
        # await bot.send_video(message.chat.id, video=video_url)
        await callback.message.answer(text=f'Время на получение ссылки {video_url} на видео: {time_end - time_start}')
    else:
        print('Ссылка на видео НЕ полуена в Хэндлере')
        await callback.message.answer(text='Ошибка получения ссылки на видео (см. логи)')
    

@router.callback_query(Text(startswith='requests'))
async def process_requests_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    shortcode = callback.data.split(' ')[-1]
    print(shortcode)
    caption, video_url = get_video_requests(shortcode)
    if video_url:
        video_url = video_url[:50]
        time_end = datetime.now()
        print(video_url)
        print('Ссылка на видео полуена в Хэндлере')
        # await bot.send_video(message.chat.id, video=video_url)
        await callback.message.answer(text=f'Время на получение ссылки {video_url} на видео: {time_end - time_start}')
    else:
        print('Ссылка на видео НЕ полуена в Хэндлере')
        await callback.message.answer(text='Ошибка получения ссылки на видео (см. логи)')


@router.callback_query(Text(startswith='instagrapi'))
async def process_requests_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    shortcode = callback.data.split(' ')[-1]
    print(shortcode)
    video_url = get_video_instagrapi(shortcode)
    if video_url:
        video_url = video_url[:50]
        time_end = datetime.now()
        print(video_url)
        print('Ссылка на видео полуена в Хэндлере')
        # await bot.send_video(message.chat.id, video=video_url)
        await callback.message.answer(text=f'Время на получение ссылки {video_url} на видео: {time_end - time_start}')
    else:
        print('Ссылка на видео НЕ полуена в Хэндлере')
        await callback.message.answer(text='Ошибка получения ссылки на видео (login_required)')


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message, bot: Bot):
    fname = message.from_user.first_name
    lname = message.from_user.last_name
    tg_id = message.from_user.id
    await message.answer(
        text=MESSAGE[lang]['START_MESSAGE'])

