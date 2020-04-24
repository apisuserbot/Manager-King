from io import BytesIO
import html
from time import sleep
from typing import Optional, List
from telegram import TelegramError, Chat, Message
from telegram import Update, Bot
from telegram.error import BadRequest
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown
from html import escape
from emilia.modules.helper_funcs.chat_status import is_user_ban_protected, bot_admin
from emilia.modules.disable import DisableAbleCommandHandler

import emilia.modules.sql.users_sql as sql
from emilia import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, LOGGER
from emilia.modules.helper_funcs.filters import CustomFilters

USERS_GROUP = 4


def escape_html(word):
    return escape(word)


@run_async
def quickscope(update, context: List[int]):
    args = context.args
    if args:
        chat_id = str(args[1])
        to_kick = str(args[0])
    else:
        update.effective_message.reply_text("You don't seem to be referring to a chat/user")
    try:
        bot.kick_chat_member(chat_id, to_kick)
        update.effective_message.reply_text("Attempted banning " + to_kick + " from" + chat_id)
    except BadRequest as excp:
        update.effective_message.reply_text(excp.message + " " + to_kick)


@run_async
def quickunban(update, context: List[int]):
    args = context.args
    if args:
        chat_id = str(args[1])
        to_kick = str(args[0])
    else:
        update.effective_message.reply_text("You don't seem to be referring to a chat/user")
    try:
        bot.unban_chat_member(chat_id, to_kick)
        update.effective_message.reply_text("Attempted unbanning " + to_kick + " from" + chat_id)
    except BadRequest as excp:
        update.effective_message.reply_text(excp.message + " " + to_kick)


@run_async
def banall(update, context: List[int]):
    args = context.args
    if args:
        chat_id = str(args[0])
        all_mems = sql.get_chat_members(chat_id)
    else:
        chat_id = str(update.effective_chat.id)
        all_mems = sql.get_chat_members(chat_id)
    for mems in all_mems:
        try:
            context.bot.kick_chat_member(chat_id, mems.user)
            update.effective_message.reply_text("Tried banning " + str(mems.user))
            sleep(0.1)
        except BadRequest as excp:
            update.effective_message.reply_text(excp.message + " " + str(mems.user))
            continue


@run_async
def snipe(update, context: List[str]):
    args = context.args
    try:
        chat_id = str(args[0])
        del args[0]
    except TypeError as excp:
        update.effective_message.reply_text("Please give me a chat to echo to!")
    to_send = " ".join(args)
    if len(to_send) >= 2:
        try:
            context.bot.sendMessage(int(chat_id), str(to_send))
        except TelegramError:
            LOGGER.warning("Couldn't send to group %s", str(chat_id))
            update.effective_message.reply_text("Couldn't send the message. Perhaps I'm not part of that group?")



@bot_admin
def leavechat(update, context: List[int]):
    args = context.args
    if args:
        chat_id = int(args[0])
    else:
        update.effective_message.reply_text("You do not seem to be referring to a chat!")
    try:
        chat = bot.getChat(chat_id)
        titlechat = bot.get_chat(chat_id).title
        context.bot.sendMessage(chat_id, "`I Go Away!`")
        bot.leaveChat(chat_id)
        update.effective_message.reply_text("I left group {}".format(titlechat))

    except BadRequest as excp:
        if excp.message == "Chat not found":
            update.effective_message.reply_text("It looks like I've been kicked out of the group :p")
        else:
            return

@run_async
def slist(update, context):
    message = update.effective_message
    text1 = "My sudo users are:"
    text2 = "My support users are:"
    for user_id in SUDO_USERS:
        try:
            user = context.bot.get_chat(user_id)
            name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)
            if user.username:
                name = escape_html("@" + user.username)
            text1 += "\n - `{}`".format(name)
        except BadRequest as excp:
            if excp.message == 'Chat not found':
                text1 += "\n - ({}) - not found".format(user_id)
    for user_id in SUPPORT_USERS:
        try:
            user = context.bot.get_chat(user_id)
            name = "[{}](tg://user?id={})".format(user.first_name + (user.last_name or ""), user.id)
            if user.username:
                name = escape_html("@" + user.username)
            text2 += "\n - `{}`".format(name)
        except BadRequest as excp:
            if excp.message == 'Chat not found':
                text2 += "\n - ({}) - not found".format(user_id)
    message.reply_text(text1 + "\n", parse_mode=ParseMode.MARKDOWN)
    message.reply_text(text2 + "\n", parse_mode=ParseMode.MARKDOWN)

__help__ = """
**Owner only:**
- /getlink **chatid**: Get the invite link for a specific chat.
- /banall: Ban all members from a chat
- /snipe **chatid** **string**: Make me send a message to a specific chat.
- /leavechat **chatid** : leave a chat
**Sudo/owner only:**
- /quickscope **userid** **chatid**: Ban user from chat.
- /quickunban **userid** **chatid**: Unban user from chat.
- /stats: check bot's stats
- /chatlist: get chatlist
- /gbanlist: get gbanned users list
- Chat bans via /restrict chat_id and /unrestrict chat_id commands
**Support user:**
- /gban : Global ban a user
- /ungban : Ungban a user
Sudo/owner can use these commands too.
**Users:**
- /slist Gives a list of sudo and support users
"""

__mod_name__ = "SpecialOPS"

SNIPE_HANDLER = DisableAbleCommandHandler("snipe", snipe, pass_args=True, filters=Filters.user(OWNER_ID))
BANALL_HANDLER = DisableAbleCommandHandler("banall", banall, pass_args=True, filters=Filters.user(OWNER_ID))
QUICKSCOPE_HANDLER = DisableAbleCommandHandler("quickscope", quickscope, pass_args=True, filters=CustomFilters.sudo_filter)
QUICKUNBAN_HANDLER = DisableAbleCommandHandler("quickunban", quickunban, pass_args=True, filters=CustomFilters.sudo_filter)

LEAVECHAT_HANDLER = DisableAbleCommandHandler("leavechat", leavechat, pass_args=True, filters=Filters.user(OWNER_ID))
SLIST_HANDLER = DisableAbleCommandHandler("slist", slist,
                           filters=CustomFilters.sudo_filter | CustomFilters.support_filter)

dispatcher.add_handler(SNIPE_HANDLER)
dispatcher.add_handler(BANALL_HANDLER)
dispatcher.add_handler(QUICKSCOPE_HANDLER)
dispatcher.add_handler(QUICKUNBAN_HANDLER)

dispatcher.add_handler(LEAVECHAT_HANDLER)
dispatcher.add_handler(SLIST_HANDLER)
