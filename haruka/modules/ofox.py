import datetime
import hashlib
import io
import os
import re
import subprocess
import time

from haruka.modules.disable import DisableAbleCommandHandler
from typing import Optional, List
from telegram import Message, Chat, Update, Bot, User
from telegram.ext.dispatcher import run_async
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# Constants
FOX_CHATS = [483808054, -1001287179850, -1001280218923, -1001155400138, -1001362128194]
FOX_BETA_CHATS = [-1001280218923, -1001362128194, 483808054]
FOX_DEV_CHAT = -1001155400138
FOX_DOMAIN = 'https://files.orangefox.tech/'

FOX_STABLE_CHANNEL = -1001196811863
FOX_BETA_CHANNEL = -1001429093106

@run_async
async def get_build_info(bot: Bot, update: Update, args: List[str]) -> str:
    codename = message.text.split('@LordHitsuki_BOT')[0][1:].lower()

    chat_id = message.chat.id
    chat_type = 'stable'
    files_dir = 'OrangeFox-Stable/'
    text = ''
    if chat_id in FOX_BETA_CHATS:
        text = '<b>OrangeFox Recovery Beta</b>\n'
        chat_type = 'beta'
        files_dir = 'OrangeFox-Beta/'
        return

    last_build = device[chat_type + "_build"]

    text += f"📱 <b>{device['fullname']}</b> (<code>{device['codename']}</code>)"
    text += f'\n📄 Last {chat_type} build: <code>{last_build}</code>'
    date_str = datetime.datetime.fromtimestamp(device[f'{chat_type}_date']).strftime('%a %b %d %H:%M %Y')
    text += f'\n📅 Date: <code>{date_str}</code>'
    text += f"\n👨‍🔬 Maintainer: {device['maintainer']}"

    if 'status' in device:
        text += f", status: <code>{device['status']}</code>"

    if f'{chat_type}_md5' in device:
        text += f"\n✅ File MD5: <code>{device[chat_type + '_md5']}</code>"

    if f'{chat_type}_build_bugs' in device:
        text += f'\n🐞 Build Bugs:\n' + device[chat_type + '_build_bugs']

    if f'{chat_type}_special_notes' in device:
        text += f'\n📝 Build Notes:\n' + device[chat_type + '_special_notes']

    if os.path.exists(FOX_FILES_LOCAL + files_dir + codename + '/' + last_build[:-3] + 'txt'):
        text += f"\n<a href=\"{FOX_DOMAIN + files_dir + codename + '/' + last_build[:-3] + 'txt'}\">🗒 View changelog and more info</a>"

    buttons = InlineKeyboardMarkup().add(
        InlineKeyboardButton("⬇️ Download this build", url=FOX_DOMAIN + files_dir + codename + '/' + last_build)
    )

    if f'{chat_type}_sf' in device and device[f'{chat_type}_sf'] is True:
        print('owo')
        buttons.add(InlineKeyboardButton("🗄️ All builds", url=FOX_DOMAIN + files_dir))
        sf_url = 'https://sourceforge.net/projects/orangefox/files/' + codename + '/' + last_build
        buttons.insert(InlineKeyboardButton("☁️ Cloud", url=sf_url))
    else:
        buttons.insert(InlineKeyboardButton("🗄️ All builds", url=FOX_DOMAIN + files_dir))

    msg = await message.reply(text, reply_markup=buttons, disable_web_page_preview=True)


__help__ = """
"""

__mod_name__ = "AFK"

GET_BUILD_INFO_HANDLER = DisableAbleCommandHandler("ofox", get_build_info)

dispatcher.add_handler(GET_BUILD_INFO_HANDLER)
