from telegram import ChatAction
from gtts import gTTS
import html
import urllib.request
import re
import json
from datetime import datetime
from typing import Optional, List
import time
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from emilia import dispatcher
from emilia.modules.disable import DisableAbleCommandHandler
from emilia.modules.helper_funcs.extraction import extract_user

def tti(update, context):
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    filename = datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    tti = gTTS(reply, lang='id')
    tti.save("k.mp3")
    with open("k.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        tti = gTTS(reply, lang='id')
        tti.save("k.mp3")
    with open("k.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)

def tte(update, context):
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    filename = datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    tte = gTTS(reply, lang='en')
    tte.save("t.mp3")
    with open("t.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        tte = gTTS(reply, lang='en')
        tte.save("t.mp3")
    with open("t.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)

def ttj(update, context):
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    filename = datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    ttj = gTTS(reply, lang='jw')
    ttj.save("j.mp3")
    with open("j.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        ttj = gTTS(reply, lang='jw')
        ttj.save("j.mp3")
    with open("j.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)

def tts(update, context):
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    filename = datetime.now().strftime("%d%m%y-%H%M%S%f")
    reply = " ".join(args)
    update.message.chat.send_action(ChatAction.RECORD_AUDIO)
    tts = gTTS(reply, lang='su')
    tts.save("su.mp3")
    with open("su.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        update.message.chat.send_action(ChatAction.RECORD_AUDIO)
        tts = gTTS(reply, lang='su')
        tts.save("su.mp3")
    with open("su.mp3", "rb") as speech:
        update.message.reply_voice(speech, quote=False)

__help__ = """
 - /tti <any text> : Converts text to speech in Indonesian Language.
 - /tts <any text> : Converts text to speech in Sundanese Language.
 - /ttj <any text> : Converts text to speech in Javanese Language.
 - /tte <any text> : Converts text to speech in English Language.
"""

__mod_name__ = "Text to Speech"

dispatcher.add_handler(DisableAbleCommandHandler("tts", tts, pass_args=True))
dispatcher.add_handler(DisableAbleCommandHandler("ttj", ttj, pass_args=True))
dispatcher.add_handler(DisableAbleCommandHandler("tte", tte, pass_args=True))
dispatcher.add_handler(DisableAbleCommandHandler("tti", tti, pass_args=True))
