import subprocess
import os

import haruka.modules.helper_funcs.cas_api as cas
import haruka.modules.helper_funcs.git_api as git

from platform import python_version
from telegram import Update, Bot, Message, Chat, ParseMode
from telegram.ext import CommandHandler, run_async, Filters

from haruka import dispatcher, OWNER_ID, SUDO_USERS
from haruka.modules.helper_funcs.filters import CustomFilters
from haruka.modules.disable import DisableAbleCommandHandler

def pingme():
    out = ""
    under = False
    if os.name == 'nt':
        output = subprocess.check_output("ping -n 1 1.0.0.1 | findstr time*", shell=True).decode()
        outS = output.splitlines()
        out = outS[0]
    else:
        out = subprocess.check_output("ping -c 1 1.0.0.1 | grep time=", shell=True).decode()
    splitOut = out.split(' ')
    stringtocut = ""
    for line in splitOut:
        if(line.startswith('time=') or line.startswith('time<')):
            stringtocut=line
            break
    newstra=stringtocut.split('=')
    if len(newstra) == 1:
        under = True
        newstra=stringtocut.split('<')
    newstr=""
    if os.name == 'nt':
        newstr=newstra[1].split('ms')
    else:
        newstr=newstra[1].split(' ') #redundant split, but to try and not break windows ping
    ping_time = float(newstr[0])
    return ping_time

@run_async
def status(bot: Bot, update: Update):
    #pingSpeed = pingme()
    reply = "<b>System Status:</b> <code>operational</code>\n\n"
    reply += "<b>Python version:</b> <code>"+python_version()+"</code>\n"
    #reply += "Ping speed: "+str(pingSpeed)+"ms\n"
    reply += "<b>CAS API version:</b> <code>"+str(cas.vercheck())+"</code>\n"
    reply += "<b>GitHub API version:</b> <code>"+str(git.vercheck())+"</code>\n"
    update.effective_message.reply_text(reply, parse_mode=ParseMode.HTML)


STATUS_HANDLER = CommandHandler("status", status, filters=CustomFilters.sudo_filter)

dispatcher.add_handler(STATUS_HANDLER)
