import asyncio

import aiohttp
from telegram import Update, Bot
from telegram.ext import run_async

from emilia import dispatcher, DOG_API_KEY, CAT_API_KEY
from emilia.modules.disable import DisableAbleCommandHandler

DOG_URL = 'http://api.thedogapi.com/v1/images/search'
CAT_URL = 'http://api.thecatapi.com/v1/images/search'


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
def dog(update, context):
    loop = asyncio.new_event_loop()
    dog = loop.run_until_complete(inuatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_photo(dog[0]["url"])


@run_async
def doghd(update, context):
    loop = asyncio.new_event_loop()
    dog = loop.run_until_complete(inuatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_document(dog[0]["url"])


@run_async
def doggif(update, context):
    loop = asyncio.new_event_loop()
    dog = loop.run_until_complete(inuatsume(loop, "gif"))
    loop.close()
    update.effective_message.reply_video(dog[0]["url"])


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
def cat(update, context):
    loop = asyncio.new_event_loop()
    cat = loop.run_until_complete(nekoatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_photo(cat[0]["url"])


@run_async
def cathd(update, context):
    loop = asyncio.new_event_loop()
    cat = loop.run_until_complete(nekoatsume(loop, "jpg,png"))
    loop.close()
    update.effective_message.reply_document(cat[0]["url"])


@run_async
def catgif(update, context):
    loop = asyncio.new_event_loop()
    cat = loop.run_until_complete(nekoatsume(loop, "gif"))
    loop.close()
    update.effective_message.reply_video(cat[0]["url"])


__help__ = "dogcat_help"

__mod_name__ = "Dogs and Cats"

if (DOG_API_KEY != None):
    DOG_HANDLER = DisableAbleCommandHandler("dog", dog, admin_ok=True, pass_args=False)
    DOGHD_HANDLER = DisableAbleCommandHandler("doghd", doghd, admin_ok=True, pass_args=False)
    DOGGIF_HANDLER = DisableAbleCommandHandler("doggif", doggif, admin_ok=True, pass_args=False)
    dispatcher.add_handler(DOG_HANDLER)
    dispatcher.add_handler(DOGHD_HANDLER)
    dispatcher.add_handler(DOGGIF_HANDLER)

if (CAT_API_KEY != None):
    CAT_HANDLER = DisableAbleCommandHandler("cat", cat, admin_ok=True, pass_args=False)
    CATHD_HANDLER = DisableAbleCommandHandler("cathd", cathd, admin_ok=True, pass_args=False)
    CATGIF_HANDLER = DisableAbleCommandHandler("catgif", catgif, admin_ok=True, pass_args=False)
    dispatcher.add_handler(CAT_HANDLER)
    dispatcher.add_handler(CATHD_HANDLER)
    dispatcher.add_handler(CATGIF_HANDLER)
