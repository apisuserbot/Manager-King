import asyncio, re, aiohttp

from telegram import Message, Update, Bot, User
from telegram.ext import Filters, MessageHandler, run_async
from haruka import dispatcher, CAT_API_KEY
from haruka.modules.disable import DisableAbleCommandHandler
from typing import List


CAT_URL = 'http://api.thecatapi.com/v1/images/search'


class catapi():
    def __init__(self, loop, type):
        headers = {"x-api-key": CAT_API_KEY}
        self.params = {"mime_types": type}
        self.session = aiohttp.ClientSession(loop=loop, headers=headers)

    async def _get(self):
        async with self.session.get(CAT_URL, params=self.params) as response:
            if response.status == 200:
                response = await response.json()
            else:
                raise Exception

        return response

    async def getcat(self):
        cat = await self._get()
        return cat

    async def close(self):
        await self.session.close()


async def nekoatsume(loop, type):
    cathouse = catapi(loop, type)
    cat = await cathouse.getcat()
    await cathouse.close()
    return cat


@run_async
def cat(bot: Bot, update: Update):
    loop = asyncio.new_event_loop()
    cat = loop.run_until_complete(nekoatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_photo(cat[0]["url"])


@run_async
def cathd(bot: Bot, update: Update):
    loop = asyncio.new_event_loop()
    cat = loop.run_until_complete(nekoatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_document(cat[0]["url"])


@run_async
def catgif(bot: Bot, update: Update):
    loop = asyncio.new_event_loop()
    cat = loop.run_until_complete(nekoatsume(loop, "gif"))
    loop.close()
    update.effective_message.reply_video(cat[0]["url"])


__help__ = """
*A module for cat lovers!*

/cat: Get pictures of cute kittens
/cathd: Get images of cute kittens in high definition
/catgif: Get gifs of cute kittens
"""

__mod_name__ = "Cats"

if (CAT_API_KEY != None):
    CAT_HANDLER = DisableAbleCommandHandler("cat", cat, admin_ok=True, pass_args=False)
    CATHD_HANDLER = DisableAbleCommandHandler("cathd", cathd, admin_ok=True, pass_args=False)
    CATGIF_HANDLER = DisableAbleCommandHandler("catgif", catgif, admin_ok=True, pass_args=False)
    dispatcher.add_handler(CAT_HANDLER)
    dispatcher.add_handler(CATHD_HANDLER)
    dispatcher.add_handler(CATGIF_HANDLER)
