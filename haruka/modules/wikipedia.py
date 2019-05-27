from telegram import ParseMode, Update, Bot
from telegram.ext import run_async

from haruka.modules.disable import DisableAbleCommandHandler
from haruka import dispatcher

from requests import get


@run_async
def wiki(bot: Bot, update: Update):
    kueri = re.split(pattern="wiki", string=update.effective_message.text)
    wikipedia.set_lang("en")
    if len(str(kueri[1])) == 0:
        update.effective_message.reply_text("Enter keywords!")
    else:
        try:
            pertama = update.effective_message.reply_text("🔄 Loading...")
            keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="🔧 More Info...", url=wikipedia.page(kueri).url)]])
            bot.editMessageText(chat_id=update.effective_chat.id, message_id=pertama.message_id, text=wikipedia.summary(kueri, sentences=10), reply_markup=keyboard)
        except wikipedia.PageError as e:
            update.effective_message.reply_text(f"⚠ Error: {e}")
        except BadRequest as et :
            update.effective_message.reply_text(f"⚠ Error: {et}")
            
            
    
__help__ = """
 - /wiki: search in wikipedia
"""

__mod_name__ = "Wikipedia"

wiki_handle = DisableAbleCommandHandler("wiki", wiki)

dispatcher.add_handler(wiki_handle)    
