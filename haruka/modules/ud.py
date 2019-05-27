from telegram import Update, Bot
from telegram.ext import run_async

from haruka.modules.disable import DisableAbleCommandHandler
from haruka import dispatcher

from requests import get

@run_async
def ud(bot: Bot, update: Update, args):
        term = ' '.join(args)
        ud_api = "http://api.urbandictionary.com/v0/define?term=" + term
        ud_reply = json.loads(requests.get(ud_api).content)['list']
        if len(args) == 0:
            update.message.reply_text("USAGE: /ud <Word>")
        elif len(ud_reply) != 0:
            ud = ud_reply[0]
            reply_text = "<b>{0}</b>\n<a href='{1}'>{1}</a>\n<i>By {2}</i>\n\nDefinition: {3}\n\nExample: {4}".format(
                ud['word'], ud['permalink'], ud['author'], ud['definition'], ud['example'])
            update.message.reply_text(reply_text, parse_mode='HTML')
        else:
            update.message.reply_text("Term not found")


__help__ = """
 - /ud:{word} Type the word or expression you want to search use. like /ud telegram Word: Telegram Definition: A once-popular system of telecommunications, in which the sender would contact the telegram service and speak their [message] over the [phone]. The person taking the message would then send it, via a teletype machine, to a telegram office near the receiver's [address]. The message would then be hand-delivered to the addressee. From 1851 until it discontinued the service in 2006, Western Union was the best-known telegram service in the world.
"""

__mod_name__ = "Urban dictionary"
  
ud_handle = DisableAbleCommandHandler("ud", ud)

dispatcher.add_handler(ud_handle)
