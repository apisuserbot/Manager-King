import html
from typing import Optional, List

import haruka.modules.helper_funcs.git_api as api

from haruka import dispatcher, OWNER_ID, LOGGER, SUDO_USERS, SUPPORT_USERS
from haruka.modules.helper_funcs.filters import CustomFilters
from haruka.modules.translations.strings import tld

from telegram.ext import CommandHandler, run_async, Filters
from telegram import Message, Chat, Update, Bot, User, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton


@run_async
def getRelease(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message
    if(len(args)<1):
        msg.reply_text("Please specify a combination of <user>/<repo>")
        return
    url = args[0]
    if not api.getData(url):
        msg.reply_text("Invalid <user>/<repo> combo")
        return
    recentRelease = api.getLastestReleaseData(api.getData(url))
    author = api.getAuthor(recentRelease)
    name = api.getReleaseName(recentRelease)
    assets = api.getAssets(recentRelease)
    releaseName = api.getReleaseName(recentRelease)
    message = "Author: "+author+"\n"
    message += "Release Name: "+releaseName+"\n\n"
    for asset in assets:
        message += "*Asset:* \n"
        fileName = api.getReleaseFileName(asset)
        fileURL = api.getReleaseFileURL(asset)
        assetFile = "[{}]({})".format(fileName, fileURL)
        sizeB = ((api.getSize(asset))/1024)/1024
        size = "{0:.2f}".format(sizeB)
        downloadCount = api.getDownloadCount(asset)
        message += assetFile + "\n"
        message += "Size: " + size + " MB"
        message += "\nDownload Count: " + str(downloadCount) + "\n\n" 
    msg.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    return


@run_async
def github(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/git '):]
    usr = get(f'https://api.github.com/users/{text}').json()
    if usr.get('login'):
        text = f"*Username:* [{usr['login']}](https://github.com/{usr['login']})"

        whitelist = ['name', 'id', 'type', 'location', 'blog',
                     'bio', 'followers', 'following', 'hireable',
                     'public_gists', 'public_repos', 'email',
                     'company', 'updated_at', 'created_at']

        difnames = {'id': 'Account ID', 'type': 'Account type', 'created_at': 'Account created at',
                    'updated_at': 'Last updated', 'public_repos': 'Public Repos', 'public_gists': 'Public Gists'}

        goaway = [None, 0, 'null', '']

        for x, y in usr.items():
            if x in whitelist:
                if x in difnames:
                    x = difnames[x]
                else:
                    x = x.title()

                if x == 'Account created at' or x == 'Last updated':
                    y = datetime.strptime(y, "%Y-%m-%dT%H:%M:%SZ")

                if y not in goaway:
                    if x == 'Blog':
                        x = "Website"
                        y = f"[Here!]({y})"
                        text += ("\n*{}:* {}".format(x, y))
                    else:
                        text += ("\n*{}:* `{}`".format(x, y))
        reply_text = text
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


@run_async
def repo(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    text = message.text[len('/repo '):]
    usr = get(f'https://api.github.com/users/{text}/repos?per_page=40').json()
    reply_text = "*Repo*\n"
    for i in range(len(usr)):
        reply_text += f"[{usr[i]['name']}]({usr[i]['html_url']})\n"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


__help__ = """
*Need some GitHub release but don't want to have to go to GitHub and go to the repository? Here are some commands that can make your life easier with GitHub.*

*Available ommands are:*
 - /git <user>/<repo>: will fetch the most recent release from that repo.
 - /git: Returns info about a GitHub user or organization.
 - /repo: Return the GitHub user or organization repository list (Limited at 40).
 
This module was only possible thanks to the [pyGitHyb_API](https://github.com/nunopenim/pyGitHyb_API)
"""

__mod_name__ = "Github"

GITHUB_HANDLER = CommandHandler("git", github, admin_ok=True)
REPO_HANDLER = CommandHandler("repo", repo, pass_args=True, admin_ok=True)
RELEASEHANDLER = CommandHandler("gitr", getRelease, pass_args=True, admin_ok=True)

dispatcher.add_handler(RELEASEHANDLER)
dispatcher.add_handler(REPO_HANDLER)
dispatcher.add_handler(GITHUB_HANDLER)
