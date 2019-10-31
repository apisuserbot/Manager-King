import asyncio, re, aiohttp

from telegram import Message, Update, Bot, User
from telegram.ext import Filters, MessageHandler, run_async
from haruka import dispatcher, DOG_API_KEY
from haruka.modules.disable import DisableAbleCommandHandler
from typing import List


DOG_URL = 'http://api.thedogapi.com/v1/images/search'


class dogapi():
    def __init__(self, loop, type):
        headers = {"x-api-key": DOG_API_KEY}
        self.params = {"mime_types": type}
        self.session = aiohttp.ClientSession(loop=loop, headers=headers)

    async def _get(self):
        async with self.session.get(DOG_URL, params=self.params) as response:
            if response.status == 200:
                response = await response.json()
            else:
                raise Exception

        return response

    async def getdog(self):
        dog = await self._get()
        return dog

    async def close(self):
        await self.session.close()


async def inuatsume(loop, type):
    doghouse = dogapi(loop, type)
    dog = await doghouse.getdog()
    await doghouse.close()
    return dog


@run_async
def dog(bot: Bot, update: Update):
    loop = asyncio.new_event_loop()
    dog = loop.run_until_complete(inuatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_photo(dog[0]["url"])


@run_async
def doghd(bot: Bot, update: Update):
    loop = asyncio.new_event_loop()
    dog = loop.run_until_complete(inuatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_document(dog[0]["url"])


@run_async
def doggif(bot: Bot, update: Update):
    loop = asyncio.new_event_loop()
    dog = loop.run_until_complete(inuatsume(loop, "gif"))
    loop.close()
    update.effective_message.reply_video(dog[0]["url"])


__help__ = """
*A module for dog lovers!*

/dog: Get pictures of cute kittens
/doghd: Get images of cute kittens in high definition
/dogif: Get gifs of cute kittens
"""

__mod_name__ = "Dogs"

if (DOG_API_KEY != None):
    DOG_HANDLER = DisableAbleCommandHandler("dog", dog, admin_ok=True, pass_args=False)
    DOGHD_HANDLER = DisableAbleCommandHandler("doghd", doghd, admin_ok=True, pass_args=False)
    DOGGIF_HANDLER = DisableAbleCommandHandler("doggif", doggif, admin_ok=True, pass_args=False)
    dispatcher.add_handler(DOG_HANDLER)
    dispatcher.add_handler(DOGHD_HANDLER)
    dispatcher.add_handler(DOGGIF_HANDLER)
