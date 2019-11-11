from typing import Optional, List

from googletrans import Translator
from telegram import Message, Update, Bot
from telegram.ext import run_async
from telegram.ext import CommandHandler

from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler


@run_async
def do_translate(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message  # type: Optional[Message]
    lan = " ".join(args)
    try:
        to_translate_text = msg.reply_to_message.text
    except:
        return
    translator = Translator()
    try:
        translated = translator.translate(to_translate_text, dest=lan)
        src_lang = translated.src
        translated_text = translated.text
        message.reply_html("<b>Translated from<\b> {} <b>to<\b> <code>{}<code>.\n {}".format(src_lang, lan, translated_text))
    except:
        msg.reply_html("<code>Error! Could not do the translation.<\code>")


__help__ = """ 
*This module uses Google Translate to do the translations.*

 - /tr (language code): as reply to a long message.
"""
__mod_name__ = "Translator"

dispatcher.add_handler(CommandHandler("tr", do_translate, pass_args=True))
