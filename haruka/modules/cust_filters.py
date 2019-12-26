import re
from typing import Optional

import telegram
from telegram import ParseMode, InlineKeyboardMarkup, Message, Chat
from telegram import Update, Bot
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown

from haruka import dispatcher, LOGGER, OWNER_ID
from haruka.modules.disable import DisableAbleCommandHandler
from haruka.modules.helper_funcs.chat_status import user_admin
from haruka.modules.helper_funcs.extraction import extract_text
from haruka.modules.helper_funcs.filters import CustomFilters
from haruka.modules.helper_funcs.misc import build_keyboard
from haruka.modules.helper_funcs.msg_types import get_filter_type
from haruka.modules.helper_funcs.string_handling import split_quotes, button_markdown_parser
from haruka.modules.sql import cust_filters_sql as sql

from haruka.modules.connection import connected

from haruka.modules.translations.strings import tld as tl
from haruka.modules.helper_funcs.alternate import send_message

HANDLER_GROUP = 10

ENUM_FUNC_MAP = {
	sql.Types.TEXT.value: dispatcher.bot.send_message,
	sql.Types.BUTTON_TEXT.value: dispatcher.bot.send_message,
	sql.Types.STICKER.value: dispatcher.bot.send_sticker,
	sql.Types.DOCUMENT.value: dispatcher.bot.send_document,
	sql.Types.PHOTO.value: dispatcher.bot.send_photo,
	sql.Types.AUDIO.value: dispatcher.bot.send_audio,
	sql.Types.VOICE.value: dispatcher.bot.send_voice,
	sql.Types.VIDEO.value: dispatcher.bot.send_video,
	sql.Types.VIDEO_NOTE.value: dispatcher.bot.send_video_note
}



@run_async
def list_handlers(bot: Bot, update: Update):
	chat = update.effective_chat  # type: Optional[Chat]
	user = update.effective_user  # type: Optional[User]
	
	conn = connected(bot, update, chat, user.id, need_admin=False)
	if not conn == False:
		chat_id = conn
		chat_name = dispatcher.bot.getChat(conn).title
		filter_list = "*List of filters in {}:*\n"
	else:
		chat_id = update.effective_chat.id
		if chat.type == "private":
			chat_name = tl(update.effective_message, "local filters")
			filter_list = tl(update.effective_message, "*local filters:*\n")
		else:
			chat_name = chat.title
			filter_list = tl(update.effective_message, "*List of filters in {}*:\n")

	all_handlers = sql.get_chat_triggers(chat_id)


	if not all_handlers:
		send_message(update.effective_message, tl(update.effective_message, "There is no filter in {}!").format(chat_name))
		return

	for keyword in all_handlers:
		entry = " - `{}`\n".format(escape_markdown(keyword))
		if len(entry) + len(filter_list) > telegram.MAX_MESSAGE_LENGTH:
			send_message(update.effective_message, filter_list.format(chat_name), parse_mode=telegram.ParseMode.MARKDOWN)
			filter_list = entry
		else:
			filter_list += entry

	send_message(update.effective_message, filter_list.format(chat_name), parse_mode=telegram.ParseMode.MARKDOWN)


# NOT ASYNC BECAUSE DISPATCHER HANDLER RAISED
@user_admin
def filters(bot: Bot, update: Update):
	chat = update.effective_chat  # type: Optional[Chat]
	user = update.effective_user  # type: Optional[User]
	msg = update.effective_message  # type: Optional[Message]
	args = msg.text.split(None, 1)  # use python's maxsplit to separate Cmd, keyword, and reply_text

	conn = connected(bot, update, chat, user.id)
	if not conn == False:
		chat_id = conn
		chat_name = dispatcher.bot.getChat(conn).title
	else:
		chat_id = update.effective_chat.id
		if chat.type == "private":
			chat_name = tl(update.effective_message, "local notes")
		else:
			chat_name = chat.title

	if not msg.reply_to_message and len(args) < 2:
		send_message(update.effective_message, tl(update.effective_message, "You must give a name for this filter!"))
		return

	if msg.reply_to_message:
		if len(args) < 2:
			send_message(update.effective_message, tl(update.effective_message, "You must give a name for this filter!"))
			return
		else:
			keyword = args[1]
	else:
		extracted = split_quotes(args[1])
		if len(extracted) < 1:
			return
		# set trigger -> lower, so as to avoid adding duplicate filters with different cases
		keyword = extracted[0].lower()
	

	# Add the filter
	# Note: perhaps handlers can be removed somehow using sql.get_chat_filters
	for handler in dispatcher.handlers.get(HANDLER_GROUP, []):
		if handler.filters == (keyword, chat_id):
			dispatcher.remove_handler(handler, HANDLER_GROUP)

	text, file_type, file_id = get_filter_type(msg)
	if not msg.reply_to_message and len(extracted) >= 2:
		offset = len(extracted[1]) - len(msg.text)  # set correct offset relative to command + notename
		text, buttons = button_markdown_parser(extracted[1], entities=msg.parse_entities(), offset=offset)
		text = text.strip()
		if not text:
			send_message(update.effective_message, tl(update.effective_message, "There is no note message - You can't JUST have buttons, you need a message to go with it!"))
			return

	elif msg.reply_to_message and len(args) >= 2:
		if msg.reply_to_message.text:
			text_to_parsing = msg.reply_to_message.text
		elif msg.reply_to_message.caption:
			text_to_parsing = msg.reply_to_message.caption
		else:
			text_to_parsing = ""
		offset = len(text_to_parsing)  # set correct offset relative to command + notename
		text, buttons = button_markdown_parser(text_to_parsing, entities=msg.parse_entities(), offset=offset)
		text = text.strip()

	elif not text and not file_type:
		send_message(update.effective_message, tl(update.effective_message, "You must give a name for this filter!"))
		return

	elif msg.reply_to_message:
		if msg.reply_to_message.text:
			text_to_parsing = msg.reply_to_message.text
		elif msg.reply_to_message.caption:
			text_to_parsing = msg.reply_to_message.caption
		else:
			text_to_parsing = ""
		offset = len(text_to_parsing)  # set correct offset relative to command + notename
		text, buttons = button_markdown_parser(text_to_parsing, entities=msg.parse_entities(), offset=offset)
		text = text.strip()
		if (msg.reply_to_message.text or msg.reply_to_message.caption) and not text:
			send_message(update.effective_message, tl(update.effective_message, "There is no message - you cannot ONLY push a button, you need a message to do it!"))
			return

	else:
		send_message(update.effective_message, tl(update.effective_message, "Invalid filter!"))
		return

	sql.new_add_filter(chat_id, keyword, text, file_type, file_id, buttons)
	# This is an old method
	# sql.add_filter(chat_id, keyword, content, is_sticker, is_document, is_image, is_audio, is_voice, is_video, buttons)

	send_message(update.effective_message, tl(update.effective_message, "Handler '{}' added in *{}*!").format(keyword, chat_name), parse_mode=telegram.ParseMode.MARKDOWN)
	raise DispatcherHandlerStop


# NOT ASYNC BECAUSE DISPATCHER HANDLER RAISED
@user_admin
def stop_filter(bot: Bot, update: Update):
	chat = update.effective_chat  # type: Optional[Chat]
	user = update.effective_user  # type: Optional[User]
	args = update.effective_message.text.split(None, 1)
	
	conn = connected(bot, update, chat, user.id)
	if not conn == False:
		chat_id = conn
		chat_name = dispatcher.bot.getChat(conn).title
	else:
		chat_id = update.effective_chat.id
		if chat.type == "private":
			chat_name = tl(update.effective_message, "local note")
		else:
			chat_name = chat.title

	if len(args) < 2:
		send_message(update.effective_message, tl(update.effective_message, "What should i stop?"))
		return

	chat_filters = sql.get_chat_triggers(chat_id)

	if not chat_filters:
		send_message(update.effective_message, tl(update.effective_message, "There are no active filters here!"))
		return

	for keyword in chat_filters:
		if keyword == args[1]:
			sql.remove_filter(chat_id, args[1])
			send_message(update.effective_message, tl(update.effective_message, "Yes, I will stop answering it at *{}*.").format(chat_name), parse_mode=telegram.ParseMode.MARKDOWN)
			raise DispatcherHandlerStop

	send_message(update.effective_message, "That's not an active filter - run /filters for all active filters.")


@run_async
def reply_filter(bot: Bot, update: Update):
	chat = update.effective_chat  # type: Optional[Chat]
	message = update.effective_message  # type: Optional[Message]

	to_match = extract_text(message)
	if not to_match:
		return

	chat_filters = sql.get_chat_triggers(chat.id)
	for keyword in chat_filters:
		pattern = r"( |^|[^\w])" + re.escape(keyword) + r"( |$|[^\w])"
		if re.search(pattern, to_match, flags=re.IGNORECASE):
			filt = sql.get_filter(chat.id, keyword)
			if filt.reply == "there is should be a new reply":
				buttons = sql.get_buttons(chat.id, filt.keyword)
				keyb = build_keyboard(buttons)
				keyboard = InlineKeyboardMarkup(keyb)
				if filt.file_type in (sql.Types.BUTTON_TEXT, sql.Types.TEXT):
					try:
						bot.send_message(chat.id, filt.reply_text, reply_to_message_id=message.message_id,
										 parse_mode="markdown", disable_web_page_preview=True,
										 reply_markup=keyboard)
					except BadRequest as excp:
						error_catch = get_exception(excp, filt, chat)
						if error_catch == "noreply":
							try:
								bot.send_message(chat.id, filt.reply_text, parse_mode="markdown", disable_web_page_preview=True, reply_markup=keyboard)
							except BadRequest as excp:
								LOGGER.exception("Failed to send message: " + excp.message)
								send_message(update.effective_message, tl(update.effective_message, get_exception(excp, filt, chat)))
								pass
						else:
							try:
								send_message(update.effective_message, tl(update.effective_message, get_exception(excp, filt, chat)))
							except BadRequest as excp:
								LOGGER.exception("Failed to send message: " + excp.message)
								pass
				else:
					ENUM_FUNC_MAP[filt.file_type](chat.id, filt.file_id, caption=filt.reply_text, reply_to_message_id=message.message_id, parse_mode="markdown", disable_web_page_preview=True, reply_markup=keyboard)
				break
			else:
				if filt.is_sticker:
					message.reply_sticker(filt.reply)
				elif filt.is_document:
					message.reply_document(filt.reply)
				elif filt.is_image:
					message.reply_photo(filt.reply)
				elif filt.is_audio:
					message.reply_audio(filt.reply)
				elif filt.is_voice:
					message.reply_voice(filt.reply)
				elif filt.is_video:
					message.reply_video(filt.reply)
				elif filt.has_markdown:
					buttons = sql.get_buttons(chat.id, filt.keyword)
					keyb = build_keyboard(buttons)
					keyboard = InlineKeyboardMarkup(keyb)

					try:
						send_message(update.effective_message, filt.reply, parse_mode=ParseMode.MARKDOWN,
										   disable_web_page_preview=True,
										   reply_markup=keyboard)
					except BadRequest as excp:
						if excp.message == "Unsupported url protocol":
							try:
								send_message(update.effective_message, tl(update.effective_message, "You seem to be trying to use an url protocol that is not supported. Telegram "
												   "does not support keys for some protocols, such as tg://. Please try "
												   "again."))
							except BadRequest as excp:
								LOGGER.exception("Failed to send message: " + excp.message)
								pass
						elif excp.message == "Reply message not found":
							try:
								bot.send_message(chat.id, filt.reply, parse_mode=ParseMode.MARKDOWN,
												 disable_web_page_preview=True,
												 reply_markup=keyboard)
							except BadRequest as excp:
								LOGGER.exception("Failed to send message: " + excp.message)
								pass
						else:
							try:
								send_message(update.effective_message, tl(update.effective_message, "This note cannot be sent because it is in the wrong format."))
							except BadRequest as excp:
								LOGGER.exception("Failed to send message: " + excp.message)
								pass
							LOGGER.warning("Message %s could not be parsed", str(filt.reply))
							LOGGER.exception("Could not parse filter %s in chat %s", str(filt.keyword), str(chat.id))

				else:
					# LEGACY - all new filters will have has_markdown set to True.
					try:
						send_message(update.effective_message, filt.reply)
					except BadRequest as excp:
						LOGGER.exception("Failed to send message: " + excp.message)
						pass
				break


def get_exception(excp, filt, chat):
	if excp.message == "Unsupported url protocol":
		return "You seem to be trying to use an url protocol that is not supported. Telegram does not support keys for some protocols, such as tg://. Please try again later."
	elif excp.message == "Reply message not found":
		return "noreply"
	else:
		LOGGER.warning("Message %s could not be parsed", str(filt.reply))
		LOGGER.exception("Could not parse filter %s in chat %s", str(filt.keyword), str(chat.id))
		return "This note cannot be sent because it is in the wrong format."


def __stats__():
	return "{} filters, across {} chats.".format(sql.num_filters(), sql.num_chats())


def __import_data__(chat_id, data):
	# set chat filters
	filters = data.get('filters', {})
	for trigger in filters:
		sql.add_to_blacklist(chat_id, trigger)


def __migrate__(old_chat_id, new_chat_id):
	sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
	cust_filters = sql.get_chat_triggers(chat_id)
	return tl(user_id, "There are `{}` custom filters here.").format(len(cust_filters))


__help__ = """
Make your chat more lively with filters; The bot will reply to certain words!
Filters are case insensitive; every time someone says your trigger words, {} will reply something else! can be used to create your own commands, if desired.
 - /filters: list all active filters in this chat.
*Admin only:*
 - /filter <keyword> <reply message>: Every time someone says "word", the bot will reply with "sentence". For multiple word filters, quote the first word.
 - /stop <filter keyword>: stop that filter.
 
 An example of how to set a filter would be via:
`/filter hello Hello there! How are you?`
A multiword filter could be set via:
`/filter "hello friend" Hello back! Long time no see!`
If you want to save an image, gif, or sticker, or any other data, do the following:
`/filter word`, while replying to a sticker or whatever data you'd like. Now, every time someone mentions "word", that sticker will be sent as a reply.
Now, anyone saying "hello" will be replied to with "Hello there! How are you?".
"""

__mod_name__ = "Filters"

FILTER_HANDLER = CommandHandler("filter", filters)
STOP_HANDLER = CommandHandler("stop", stop_filter)
LIST_HANDLER = DisableAbleCommandHandler("filters", list_handlers, admin_ok=True)
CUST_FILTER_HANDLER = MessageHandler(CustomFilters.has_text, reply_filter)

dispatcher.add_handler(FILTER_HANDLER)
dispatcher.add_handler(STOP_HANDLER)
dispatcher.add_handler(LIST_HANDLER)
dispatcher.add_handler(CUST_FILTER_HANDLER, HANDLER_GROUP)
