import json
import re
from datetime import datetime
from typing import List

import yaml
from bs4 import BeautifulSoup
from hurry.filesize import size as sizee
from requests import get
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram import Update, Bot
from telegram.ext import CommandHandler
from telegram.ext import run_async

from haruka import dispatcher, LOGGER

# DO NOT DELETE THIS, PLEASE.
# Originally made by @RealAkito on GitHub and Telegram.
# This module was inspired by Android Helper Bot by Vachounet.
# None of the code is taken from the bot itself, to avoid any more confusion.

LOGGER.info("Original Android Modules by @RealAkito on Telegram, modified by @HitaloSama on Telegram")

GITHUB = 'https://github.com'
DEVICES_DATA = 'https://raw.githubusercontent.com/androidtrackers/certified-android-devices/master/devices.json'


@run_async
def device(bot, update, args):
    if len(args) == 0:
        update.effective_message.reply_text("No codename provided, write a codename for fetching informations.")
        return
    device = " ".join(args)
    found = [
        i for i in get(DEVICES_DATA).json()
        if i["device"] == device or i["model"] == device
    ]
    if found:
        reply = f'Search results for {device}:\n\n'
        for item in found:
            brand = item['brand']
            name = item['name']
            codename = item['device']
            model = item['model']
            reply += f'<b>{brand} {name}</b>\n' \
                     f'Model: <code>{model}</code>\n' \
                     f'Codename: <code>{codename}</code>\n\n'
    else:
        reply = f"Couldn't find info about {device}!\n"
    update.message.reply_text("{}".format(reply),
                              parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@run_async
def magisk(bot, update):
    url = 'https://raw.githubusercontent.com/topjohnwu/magisk_files/'
    releases = ""
    for type, path in {"Stable": "master/stable", "Beta": "master/beta", "Canary": "canary/release"}.items():
        data = get(url + path + '.json').json()
        releases += f'{type}: [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | ' \
                    f'[APP v{data["app"]["version"]}]({data["app"]["link"]}) | ' \
                    f'[Uninstaller]({data["uninstaller"]["link"]})\n'

    update.message.reply_text("*Latest Magisk Releases:*\n{}".format(releases),
                              parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


def twrp(bot, update, args):
    if len(args) == 0:
        update.effective_message.reply_text("No codename provided, write a codename for fetching informations.")
        return
    device = " ".join(args)
    url = get(f'https://dl.twrp.me/{device}/')
    if url.status_code == 404:
        reply = f"Couldn't find twrp downloads for {device}!\n"
        return
    reply = f'*Latest Official TWRP for {device}*\n'
    db = get(DEVICES_DATA).json()
    newdevice = device.strip('lte') if device.startswith('beyond') else device
    for dev in db:
        if (dev['device'] == newdevice) or (dev['model'] == newdevice):
            brand = dev['brand']
            name = dev['name']
            reply += f'*{brand} - {name}*\n'
            break
    page = BeautifulSoup(url.content, 'lxml')
    date = page.find("em").text.strip()
    reply += f'*Updated:* {date}\n'
    trs = page.find('table').find_all('tr')
    row = 2 if trs[0].find('a').text.endswith('tar') else 1
    for i in range(row):
        download = trs[i].find('a')
        dl_link = f"https://dl.twrp.me{download['href']}"
        dl_file = download.text
        size = trs[i].find("span", {"class": "filesize"}).text
        reply += f'[{dl_file}]({dl_link}) - {size}\n'

    update.message.reply_text("{}".format(reply),
                              parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def aex(bot: Bot, update: Update, args: List[str]):
    AEX_OTA_API = "https://api.aospextended.com/ota/"
    message = update.effective_message

    if len(args) != 2:
        reply_text = "Please type your device **codename** and **Android Version**!\nFor example, `/aex jason pie`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    device = args[0]
    version = args[1]
    res = get(AEX_OTA_API + device + '/' + version.lower())
    if res.status_code == 200:
        apidata = json.loads(res.text)
        if apidata.get('error'):
            message.reply_text("Sorry, but there isn't any build available for " + device)
            return
        else:
            developer = apidata.get('developer')
            developer_url = apidata.get('developer_url')
            forum_url = apidata.get('forum_url')
            filename = apidata.get('filename')
            url = "https://downloads.aospextended.com/download/" + device + "/" + version + "/" + apidata.get(
                'filename')
            builddate = datetime.strptime(apidata.get('build_date'), "%Y%m%d-%H%M").strftime("%d %B %Y")
            buildsize = sizee(int(apidata.get('filesize')))

            message = (f"*Download:* [{filename}]({url})\n"
                       f"*Build date:* `{builddate}`\n"
                       f"*Build size:* `{buildsize}`\n"
                       f"*XDA Thread:* [Here]({forum_url})\n"
                       f"*By:* [{developer}]({developer_url})\n")

            keyboard = [[InlineKeyboardButton(text="Click here to download", url=f"{url}")]]
            update.effective_message.reply_text(message, reply_markup=InlineKeyboardMarkup(keyboard),
                                                parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
            return
    else:
        message.reply_text("No builds found for the provided device-version combo.")


@run_async
def bootleggers(bot: Bot, update: Update):
    message = update.effective_message
    codename = message.text[len('/bootleggers '):]

    if codename == '':
        reply_text = "Please type your device **codename**!\nFor example, `/bootleggers tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get('https://bootleggersrom-devices.github.io/api/devices.json')
    if fetch.status_code == 200:
        nestedjson = fetch.json()

        if codename.lower() == 'x00t':
            devicetoget = 'X00T'
        else:
            devicetoget = codename.lower()

        reply_text = ""
        devices = {}

        for device, values in nestedjson.items():
            devices.update({device: values})

        if devicetoget in devices:
            for oh, baby in devices[devicetoget].items():
                dontneedlist = ['id', 'filename', 'download', 'xdathread']
                peaksmod = {'fullname': 'Device name', 'buildate': 'Build date', 'buildsize': 'Build size',
                            'downloadfolder': 'SourceForge folder', 'mirrorlink': 'Mirror link',
                            'xdathread': 'XDA thread'}
                if baby and oh not in dontneedlist:
                    if oh in peaksmod:
                        oh = peaksmod[oh]
                    else:
                        oh = oh.title()

                    if oh == 'SourceForge folder':
                        reply_text += f"\n*{oh}:* [Here]({baby})"
                    elif oh == 'Mirror link':
                        reply_text += f"\n*{oh}:* [Here]({baby})"
                    else:
                        reply_text += f"\n*{oh}:* `{baby}`"

            reply_text += f"\n*XDA Thread:* [Here]({devices[devicetoget]['xdathread']})"
            reply_text += f"\n*Download:* [{devices[devicetoget]['filename']}]({devices[devicetoget]['download']})"
            reply_text = reply_text.strip("\n")
        else:
            reply_text = 'Device not found.'

    elif fetch.status_code == 404:
        reply_text = "Couldn't reach Bootleggers API."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def dotos(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/dotos '):]

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/dotos tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get(f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json')
    if fetch.status_code == 200:
        usr = fetch.json()
        response = usr['response'][0]
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        version = response['version']
        changelog = response['changelog_device']

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`\n"
                      f"*Device Changelog:* `{changelog}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    elif fetch.status_code == 404:
        reply_text = "Device not found"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def evo(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/evo '):]

    if device == "x00t" or device == "x01bd":
        device = device.upper()

    fetch = get(f'https://raw.githubusercontent.com/Evolution-X-Devices/official_devices/master/builds/{device}.json')

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/evo tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    if device == 'gsi':
        reply_text = "Please check TeamGSIs channel(@TeamGSI) for unofficial but updated GSIs" \
                     " or click the button down to download the official GSIs!"

        keyboard = [[InlineKeyboardButton(text="Click to Download",
                                          url="https://sourceforge.net/projects/evolution-x/files/GSI/")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    if fetch.status_code == 200:
        try:
            usr = fetch.json()
            filename = usr['filename']
            url = usr['url']
            version = usr['version']
            maintainer = usr['maintainer']
            maintainer_url = usr['telegram_username']
            size_a = usr['size']
            size_b = sizee(int(size_a))

            reply_text = (f"*Download:* [{filename}]({url})\n"
                          f"*Build Size:* `{size_b}`\n"
                          f"*Android Version:* `{version}`\n"
                          f"*Maintainer:* [{maintainer}](https://t.me/{maintainer_url})\n")

            keyboard = [[InlineKeyboardButton(text="⬇️ Download ⬇️", url=f"{url}")]]
            keyboard += [[InlineKeyboardButton(text="📃 Changelog 📃", url=f"https://raw.githubusercontent.com/Evolution-X-Devices/official_devices/master/changelogs/{device}/{filename}.txt")]]
            message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                               disable_web_page_preview=True)
            return

        except ValueError:
            reply_text = "Tell the rom maintainer to fix their OTA json. I'm sure this won't work with OTA and it won't work with this bot too :P"
            message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
            return

    elif fetch.status_code == 404:
        reply_text = "Device not found!"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return


@run_async
def havoc(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/havoc '):]
    fetch = get(f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json')

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/havoc tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    if fetch.status_code == 200:
        usr = fetch.json()
        response = usr['response'][0]
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        version = response['version']

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    elif fetch.status_code == 404:
        reply_text = "Device not found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def los(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/los '):]

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/los tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get(f'https://download.lineageos.org/api/v1/{device}/nightly/*')
    if fetch.status_code == 200 and len(fetch.json()['response']) != 0:
        usr = fetch.json()
        response = usr['response'][0]
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        version = response['version']

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    else:
        reply_text = "Device not found"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


def miui(bot: Bot, update: Update):
    giturl = "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/"
    message = update.effective_message
    device = message.text[len('/miui '):]

    if device == '':
        reply_text = "Please type your device <b>codename</b>!\nFor example, <code>/miui whyred</code>!"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    result = "<b>Recovery ROM</b>\n\n"
    result += "<b>Stable</b>\n"
    stable_all = yaml.load(get(giturl + "stable_recovery/stable_recovery.yml").content, Loader=yaml.FullLoader)
    data = [i for i in stable_all if device == i['codename']]
    if len(data) != 0:
        for i in data:
            result += "<b>Device:</b> " + i['device'] + "\n"
            result += f'<a href="{i["download"]}">{i["filename"]}</a>\n'
            result += "<b>Size:</b> " + i ['size'] + "\n"
            result += "<b>Version:</b> " + i ['version'] + "\n"
            result += "<b>Android:</b> " + i ['android'] + "\n\n"

        result += "<b>Weekly</b>\n"
        weekly_all = yaml.load(get(giturl + "weekly_recovery/weekly_recovery.yml").content, Loader=yaml.FullLoader)
        data = [i for i in weekly_all if device == i['codename']]
        for i in data:
            result += "<b>Device:</b> " + i ['device'] + "\n"
            result += f'<a href="{i["download"]}">{i["filename"]}</a>\n'
            result += "<b>Size:</b> " + i ['size'] + "\n"
            result += "<b>Version:</b> " + i ['version'] + "\n"
            result += "<b>Android:</b> " + i ['android'] + "\n\n"
    else:
        result = "Couldn't find any device matching your query."

    message.reply_html(result)


@run_async
def pe(bot: Bot, update: Update):
    message = update.effective_message
    cmd = message.text.split()[0]
    device = message.text[len(cmd)+1:]

    if device == '':
        reply_text = f"Please type your device **codename**!\nFor example, `{cmd} tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    if cmd.startswith("/peplus"):
        variant = "pie_plus"
    elif cmd.startswith("/pe10"):
        variant = "ten"
    else:
        variant = "pie"

    fetch = get(f'https://download.pixelexperience.org/ota_v3/{device}/{variant}')
    if not fetch.json()['error']:
        usr = fetch.json()
        filename = usr['filename']
        url = usr['url']
        buildsize_a = usr['size']
        buildsize_b = sizee(int(buildsize_a))
        version = usr['version']

        reply_text = (f"🔍 *PixelExperience build for {device}*\n"
                      f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=url)]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    else:
        reply_text = "Device not found"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def pearl(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/pearl '):]

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/pearl mido`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json')
    if fetch.status_code == 200:
        usr = fetch.json()
        response = usr['response'][0]
        maintainer = response['maintainer']
        romtype = response['romtype']
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        version = response['version']
        xda = response['xda']

        if xda == '':
            reply_text = (f"*Download:* [{filename}]({url})\n"
                          f"*Build size:* `{buildsize_b}`\n"
                          f"*Version:* `{version}`\n"
                          f"*Maintainer:* `{maintainer}`\n"
                          f"*ROM Type:* `{romtype}`")

            keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
            message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                               disable_web_page_preview=True)
            return

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`\n"
                      f"*Maintainer:* `{maintainer}`\n"
                      f"*ROM Type:* `{romtype}`\n"
                      f"*XDA Thread:* [Link]({xda})")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    elif fetch.status_code == 404:
        reply_text = "Device not found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def pixys(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/pixys '):]

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/pixys tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get(f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json')
    if fetch.status_code == 200:
        usr = fetch.json()
        response = usr['response'][0]
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        romtype = response['romtype']
        version = response['version']

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`\n"
                      f"*Rom Type:* `{romtype}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    elif fetch.status_code == 404:
        reply_text = "Device not found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def posp(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/posp '):]

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/posp tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly')
    if fetch.status_code == 200 and len(fetch.json()['response']) != 0:
        usr = fetch.json()
        response = usr['response'][0]
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        version = response['version']

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)
        return

    else:
        reply_text = "Device not found"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def viper(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/viper '):]

    if device == '':
        reply_text = "Please type your device **codename**!\nFor example, `/viper tissot`"
        message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
        return

    fetch = get(f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json')
    if fetch.status_code == 200:
        usr = fetch.json()
        response = usr['response'][0]
        filename = response['filename']
        url = response['url']
        buildsize_a = response['size']
        buildsize_b = sizee(int(buildsize_a))
        version = response['version']

        reply_text = (f"*Download:* [{filename}]({url})\n"
                      f"*Build size:* `{buildsize_b}`\n"
                      f"*Version:* `{version}`")

        keyboard = [[InlineKeyboardButton(text="Click to Download", url=f"{url}")]]
        message.reply_text(reply_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN,
                           disable_web_page_preview=True)

    elif fetch.status_code == 404:
        message.reply_text("Device not found")


def descendant(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    usr = get(f'https://api.github.com/repos/Descendant/InOps/releases/latest').json()
    reply_text = "*Descendant GSI Download(s)*\n"
    for i in range(len(usr)):
        try:
            name = usr['assets'][i]['name']
            url = usr['assets'][i]['browser_download_url']
            download_count = usr['assets'][i]['download_count']
            reply_text += f"[{name}]({url}) - Downloaded `{download_count}` Times\n\n"
        except IndexError:
            continue
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


def enesrelease(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    usr = get(f'https://api.github.com/repos/EnesSastim/Downloads/releases/latest').json()
    reply_text = "*Enes Sastim's lastest upload(s)*\n"
    for i in range(len(usr)):
        try:
            name = usr['assets'][i]['name']
            url = usr['assets'][i]['browser_download_url']
            reply_text += f"[{name}]({url})\n"
        except IndexError:
            continue
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


def phh(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    usr = get(f'https://api.github.com/repos/phhusson/treble_experimentations/releases/latest').json()
    reply_text = "*Phh's lastest AOSP Release(s)*\n"
    for i in range(len(usr)):
        try:
            name = usr['assets'][i]['name']
            url = usr['assets'][i]['browser_download_url']
            reply_text += f"[{name}]({url})\n"
        except IndexError:
            continue
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


def kraken(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    usr = get(f'https://api.github.com/repos/Project-Butter/KRAKEN_7870/releases').json()
    reply_text = "*Kraken Kernel lastest upload(s)*\n"
    for i in range(len(usr)):
        try:
            name = usr['assets'][i]['name']
            url = usr['assets'][i]['browser_download_url']
            reply_text += f"[{name}]({url})\n"
        except IndexError:
            continue
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


# Android Specs Module for Hitsuki Bot
@run_async
def specs(bot, update, args):
    if len(args) == 0:
        update.effective_message.reply_html("Please type your device <b>brand</b> and <b>name</b>!\
        \nFor example, <code>/specs Xiaomi Redmi Note 7</code>")
        return
    brand = args[0].lower()
    device = " ".join(args[1:]).lower()
    if brand and device:
        pass
    all_brands = BeautifulSoup(
        get('https://www.devicespecifications.com/en/brand-more').content,
        'lxml').find('div', {
            'class': 'brand-listing-container-news'
        }).findAll('a')
    try:
        brand_page_url = [
            i['href'] for i in all_brands if brand == i.text.strip().lower()
        ][0]
    except IndexError:
        update.effective_message.reply_html(f'<code>{brand}</code> is unknown brand!')
        return
    devices = BeautifulSoup(get(brand_page_url).content, 'lxml') \
        .findAll('div', {'class': 'model-listing-container-80'})
    device_page_url = [
        i.a['href']
        for i in BeautifulSoup(str(devices), 'lxml').findAll('h3')
        if device in i.text.strip().lower()
    ]
    if not device_page_url:
        update.effective_message.reply_html(f"Can't find <code>{device}</code>!")
        return
    if len(device_page_url) > 2:
        device_page_url = device_page_url[:2]
    reply = ''
    for url in device_page_url:
        info = BeautifulSoup(get(url).content, 'lxml')
        reply = '\n<b>' + info.title.text.split('-')[0].strip() + '</b>\n\n'
        info = info.find('div', {'id': 'model-brief-specifications'})
        specifications = re.findall(r'<b>.*?<br/>', str(info))
        for item in specifications:
            title = re.findall(r'<b>(.*?)</b>', item)[0].strip()
            data = re.findall(r'</b>: (.*?)<br/>', item)[0].strip()
            reply += f'<b>{title}</b>: {data}\n'
    update.effective_message.reply_html(reply)


__help__ = """
*Here you will have several useful commands for Android users!*

*Useful tools:*
 - /device <codename>: gets android device basic info from its codename
 - /magisk: gets the latest magisk release for Stable/Beta/Canary
 - /twrp <codename>: gets latest twrp for the android device using the codename
 - /specs <brand> <device name>: will give you the complete specifications of a device

 *Specific ROM for a device*
 - /aex <device> <android version>: Get the latest AEX ROM for a device
 - /bootleggers <device>: Get the latest Bootleggers ROM for a device
 - /dotos <device>: Get the latest DotOS ROM for a device
 - /evo <device>: Get the latest Evolution X ROM for a device
 - /havoc <device>: Get the latest Havoc ROM for a device
 - /los <device>: Get the latest LineageOS ROM for a device
 - /miui <device>: Get the latest MIUI ROM for a device
 - /pe <device>: Get the latest PixelExperience ROM for a device
 - /pe10 <device>: Get the latest PixelExperience 10 ROM for a device
 - /peplus <device>: Get the latest PixelExperience Plus ROM for a device
 - /pearl <device>: Get the latest Pearl ROM for a device
 - /pixys <device>: Get the latest Pixys ROM for a device
 - /posp <device>: Get the latest POSP ROM for a device
 - /viper <device>: Get the latest Viper ROM for a device
 
 *GSIs:*
 - /descendant: Get the latest Descendant GSI!
 - /enesrelease: Get the latest Enes upload
 - /phh: Get the latest Phh AOSP Oreo GSI!
 
*Kernels:*
 - /kraken: Get the latest Kraken Kernel (For Exynos 7870) uploads
"""

__mod_name__ = "Android"

DEVICE_HANDLER = CommandHandler("device", device, pass_args=True)
MAGISK_HANDLER = CommandHandler("magisk", magisk)
TWRP_HANDLER = CommandHandler("twrp", twrp, pass_args=True)
AEX_HANDLER = CommandHandler("aex", aex, pass_args=True, admin_ok=True)
BOOTLEGGERS_HANDLER = CommandHandler("bootleggers", bootleggers, admin_ok=True)
DOTOS_HANDLER = CommandHandler("dotos", dotos, admin_ok=True)
EVO_HANDLER = CommandHandler("evo", evo, admin_ok=True)
HAVOC_HANDLER = CommandHandler("havoc", havoc, admin_ok=True)
LOS_HANDLER = CommandHandler("los", los, admin_ok=True)
MIUI_HANDLER = CommandHandler("miui", miui, admin_ok=True)
PE_HANDLER = CommandHandler("pe", pe, admin_ok=True)
PE10_HANDLER = CommandHandler("pe10", pe, admin_ok=True)
PEPLUS_HANDLER = CommandHandler("peplus", pe, admin_ok=True)
PEARL_HANDLER = CommandHandler("pearl", pearl, admin_ok=True)
PIXYS_HANDLER = CommandHandler("pixys", pixys, admin_ok=True)
POSP_HANDLER = CommandHandler("posp", posp, admin_ok=True)
VIPER_HANDLER = CommandHandler("viper", viper, admin_ok=True)
DESCENDANT_HANDLER = CommandHandler("descendant", descendant, pass_args=True, admin_ok=True)
ENES_HANDLER = CommandHandler("enesrelease", enesrelease, pass_args=True, admin_ok=True)
PHH_HANDLER = CommandHandler("phh", phh, pass_args=True, admin_ok=True)
SPECS_HANDLER = CommandHandler("specs", specs, pass_args=True)
PHH_HANDLER = CommandHandler("kraken", kraken, pass_args=True, admin_ok=True)

dispatcher.add_handler(DEVICE_HANDLER)
dispatcher.add_handler(MAGISK_HANDLER)
dispatcher.add_handler(TWRP_HANDLER)
dispatcher.add_handler(AEX_HANDLER)
dispatcher.add_handler(BOOTLEGGERS_HANDLER)
dispatcher.add_handler(DOTOS_HANDLER)
dispatcher.add_handler(EVO_HANDLER)
dispatcher.add_handler(HAVOC_HANDLER)
dispatcher.add_handler(LOS_HANDLER)
dispatcher.add_handler(MIUI_HANDLER)
dispatcher.add_handler(PE_HANDLER)
dispatcher.add_handler(PE10_HANDLER)
dispatcher.add_handler(PEPLUS_HANDLER)
dispatcher.add_handler(PEARL_HANDLER)
dispatcher.add_handler(PIXYS_HANDLER)
dispatcher.add_handler(POSP_HANDLER)
dispatcher.add_handler(VIPER_HANDLER)
dispatcher.add_handler(DESCENDANT_HANDLER)
dispatcher.add_handler(ENES_HANDLER)
dispatcher.add_handler(PHH_HANDLER)
dispatcher.add_handler(SPECS_HANDLER)
dispatcher.add_handler(KRAKEN_HANDLER)
