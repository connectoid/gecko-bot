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
from services.instagram.reels.reels_requests import get_video_requests
from services.instagram.reels.reels_instagrapi import get_video_instagrapi
from services.instagram.reels.reels_selenium import get_video_selenium
from services.instagram.reels.reels_hikerapi import get_video_hikerapi
from services.instagram.stories.stories_saveig import get_stories_saveig
from services.instagram.stories.stories_ss import get_stories_ss
from services.instagram.stories.stories_hikerapi import get_story_hikerapi


storage = MemoryStorage()
router = Router()
config: Config = load_config()

lang = 'ru'
switch_reporting = True

reels_methods_buttons = [
    'Reels requests',
    'Reels video-requests',
    'Reels hikerAPI',
]

stories_methods_buttons = [
    'Stroies ssinstagram',
    'Stories hikerAPI',
]

config: Config = load_config()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

@router.message(F.text.contains('instagram.com/reel/'))
async def content_reels_requested(message: Message):
    url = message.text
    print(url)
    print(message.chat.id)
    shortcode = url.split('/reel/')[1].split('/')[0]
    await message.answer(text='Выберите метод получения ссылки на видео',
                         reply_markup=create_bottom_keyboard(reels_methods_buttons, shortcode))
    

# @router.message(F.text.contains('instagram.com/stories/'))
# async def content_stories_requested(message: Message):
#     time_start = datetime.now()
#     url = message.text
#     author = url.split('/stories/')[-1].split('/')[0]
#     author = f'@{author}'
#     print(f'Stories requested {url}')
#     print(message.chat.id)
#     stories_urls = get_stories_saveig(url)
#     if stories_urls:
#         for story_url in stories_urls:
#             await bot.send_video(
#                 message.chat.id,
#                 video=story_url,
#                 caption=author)
#         time_end = datetime.now()
#         await message.answer(text=f'Время на получение Stories: {time_end - time_start}')
#     else:
#         await message.answer(text='Ошибка получения Stories, см. логи.')

# https://www.instagram.com/stories/kaliningradru/3348976386265680364?igsh=MTZ3ZzhsM2d3YTNudQ==

@router.message(F.text.contains('instagram.com/stories/'))
async def content_stories_requested(message: Message):
    url = message.text
    print(url)
    print(message.chat.id)
    author = url.split('/stories/')[-1].split('/')[0]
    url = author + url.split(author)[-1].split('?')[0]
    print(len(url))
    print(url)
    await message.answer(text='Выберите метод получения ссылки на видео',
                         reply_markup=create_bottom_keyboard(stories_methods_buttons, url))


@router.callback_query(Text(startswith='Stroies ssinstagram'))
async def process_hikerapi_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    url = callback.data.split(' ')[-1]
    url = 'https://www.instagram.com/stories/' + url
    print(url)
    author = url.split('/stories/')[-1].split('/')[0]
    author = f'@{author}'
    print(f'Stories requested {url}')
    print(callback.message.chat.id)
    story_url = get_stories_ss(url)
    if story_url:
        # await bot.send_video(
        #     callback.message.chat.id,
        #     video=story_url,
        #     caption=author)
        time_end = datetime.now()
        story_url = story_url[:50]
        await callback.message.answer(text=f'Время на получение ссылки {story_url} на видео: {time_end - time_start}')
    else:
        await callback.message.answer(text='Ошибка получения Stories (овзможно приватный Stories), см. логи.')



@router.callback_query(Text(startswith='Stories hikerAPI'))
async def process_hikerapi_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    url = callback.data.split(' ')[-1]
    url = 'https://www.instagram.com/stories/' + url
    author = url.split('/stories/')[-1].split('/')[0]
    author = f'@{author}'
    print(url)
    stories_url = get_story_hikerapi(url)
    if stories_url:
        stories_url = stories_url[:50]
        time_end = datetime.now()
        print(stories_url)
        print('Ссылка на видео полуена в Хэндлере')
        # await bot.send_video(
        #     callback.message.chat.id,
        #     video=stories_url,
        #     caption=author
        # )
        await callback.message.answer(text=f'Время на получение ссылки {stories_url} на видео: {time_end - time_start}')
    else:
        print('Ссылка на видео НЕ полуена в Хэндлере')
        await callback.message.answer(text='Ошибка получения stories (см. логи)')



@router.callback_query(Text(startswith='selenium'))
async def process_selenium_method(callback: CallbackQuery, bot: Bot):
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
    

@router.callback_query(Text(startswith='Reels requests'))
async def process_requests_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    shortcode = callback.data.split(' ')[-1]
    print(shortcode)
    video_url = get_video_requests(shortcode)
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


@router.callback_query(Text(startswith='Reels video-requests'))
async def process_requests_videos_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    shortcode = callback.data.split(' ')[-1]
    print(shortcode)
    video_url = get_video_requests(shortcode)
    if video_url:
        video_url_cut = video_url[:50]
        time_end = datetime.now()
        print(video_url)
        print('Ссылка на видео полуена в Хэндлере')
        print(f'chat id 2: {callback.message.chat.id}')
        await bot.send_video(callback.message.chat.id, video=video_url)
        await callback.message.answer(text=f'Время на получение ссылки {video_url_cut} на видео: {time_end - time_start}')
    else:
        print('Ссылка на видео НЕ полуена в Хэндлере')
        await callback.message.answer(text='Ошибка получения ссылки на видео (см. логи)')


@router.callback_query(Text(startswith='Reels instagrapi'))
async def process_instagrapi_method(callback: CallbackQuery, bot: Bot):
    await callback.message.answer(text='Дождитесь ответа, не отправляйте следующую ссылку пока не прийдет ответ')
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


@router.callback_query(Text(startswith='Reels hikerAPI'))
async def process_hikerapi_method(callback: CallbackQuery, bot: Bot):
    time_start = datetime.now()
    shortcode = callback.data.split(' ')[-1]
    print(shortcode)
    video_url = get_video_hikerapi(shortcode)
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

