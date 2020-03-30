import requests
import os
import subprocess

import requests
import speedtest
from telegram import Update, Bot, ParseMode
from telegram.ext import CommandHandler, run_async, Filters

from emilia import dispatcher, OWNER_ID
from emilia.modules.helper_funcs.extraction import extract_text
from emilia.modules.helper_funcs.filters import CustomFilters


# Kanged from PaperPlane Extended userbot
def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

@run_async
def speedtst(update, context):
    chat = update.effective_chat
    del_msg = context.bot.send_message(chat.id, "<code>🔄 Running speedtest...</code>",
                               parse_mode=ParseMode.HTML)
    test = speedtest.Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    del_msg.delete()
    update.effective_message.reply_text("<b>SpeedTest Results</b> \n\n"
                                        "<b>Download:</b> "
                                        f"<code>{speed_convert(result['download'])}</code> \n"
                                        "<b>Upload:</b> "
                                        f"<code>{speed_convert(result['upload'])}</code> \n"
                                        "<b>Ping:</b> "
                                        f"<code>{result['ping']}</code> \n"
                                        "<b>ISP:</b> "
                                        f"<code>{result['client']['isp']}</code>",
                                        parse_mode=ParseMode.HTML)

SPEED_HANDLER = CommandHandler("speedtest", speedtst, filters=CustomFilters.sudo_filter)

dispatcher.add_handler(SPEED_HANDLER)
