import pyrogram

from helpers.ceylonnewsfactory import ceynewfac_main, ceynewfac_page
from helpers.colombotimes import colombotime_page, colombotimes_main
from helpers.common import *
from helpers.gagana import gagana_main, gagana_page
from helpers.hirunews import hiru_main, hiru_page
from helpers.lankacnews import lankacnews_main, lankacnews_page
from helpers.neth import neth_main, neth_page
from helpers.newsfirst import news_first_main, news_first_page
from helpers.penpalsnow import penpals_main
from helpers.rata import rata_main, rata_page
from helpers.sinhalanews import sinhala_news_main, sinhala_news_page
from helpers.xham import xham_main
from helpers.xvid import xvid_page_videos, xvid_search

HELP = '''
/hirunews          - 🔴 HiruNews
/newsfirst          - 🔴 NewsFirst
/gagana             - 🔴 Gagana
/ctimes              - 🔴 Col_Times
/neth                  - 🔴 NethNews
/ceyfac              - 🔴 Cey_fac
/rata                   - 🔴 Rata
/lankacnews     - 🔴 L_C_News
/sinhalanews   - 🔴 Sin_News
/help                  - 🟢 This Help
/about               - 🔸 About
/suggest           - 💝 Suggestions
**Any Question** 👉 @indexoutbound 👈'''

SUDO_HELP = '''**Any Question**👉 @indexoutbound 👈\n
/penpals_help   -> 🟡penpalsnow hint
/users                -> 🧍‍♂Send users
/logs                   -> 📝Send Logs
/featuresend     -> 📚Send features
/sendusermsg  -> 💌Send msg to All
/add                    -> 🧍‍♂Authorize
/clearusers        -> ♨️Unauthorize all
/news                 -> ⭕️Unseen news
/xhams_help     -> 🔞Xhamster help
/xvid_help          -> 🔞Xvidoes help'''

ABOUT_TEXT = """
-📌 **Bot :** `🤖_LK_News_🤖`
-📌 **Creator :** @indexoutbound 🇱🇰
-📌 **Language :** [Python3](https://python.org) 😈
-📌 **Library :** [Pyrogram v1.2.0](https://pyrogram.org) 💪
-📌 **Server :** [Heroku](https://heroku.com) 🌞
"""

EASY_HELP = '''
එක් වරක් සිරස්තල ලබාගැනීමෙන් පසුව තත්පර 5-10
කාලයක් රැදී සිට නැවත විධාන භාවිතා කරන්න. 
**නැතහොත් තාවකාලිකව මෙම සේවාව තාවකාලිකව නවතී.** 
ඔබට සිරස්තලයක වැඩිදුර තොරතුරු අවශ්‍ය නම් එම
සිරස්තලයේ ලින්කුව Copy කර send කරන්න.
'''

# - **Source :** [Click here](https://github.com/FayasNoushad/URL-Uploader)


# For checking file sending.
async def send(bot, update):
    await bot.send_photo(
        chat_id=update.chat.id,
        reply_to_message_id=update.message_id,
        photo='11.jpg',
        caption='CapTest'
    )
    await bot.send_document(
        chat_id=update.chat.id,
        reply_to_message_id=update.message_id,
        document='sample.txt',
        caption='CapTest'
    )


async def is_owner(update, reason):
    if await is_sudo(update):
        return True
    await update.reply_text("You're not the Owner😹")
    await write_log(f'{update.chat.id} tried {reason}')
    return False


@pyrogram.Client.on_message()
async def echo(bot, update):
    text = update.text.lower()

    mm = await update.reply_text('I Listen')
    sleep(1)
    await mm.delete()

    if text == '/start':
        await update.reply_text('Just Hit /help')
        return

    if text == '/about':
        await update.reply_text(ABOUT_TEXT)
        return

    if text == '/help':
        if await is_sudo(update):
            await update.reply_text(SUDO_HELP)

        await update.reply_text(HELP)
        await update.reply_text(EASY_HELP)

        return

    # if not await is_user(update):
    #     await update.reply_text("You are Not authorized😡 Ask from - @indexoutbound")
    #     return

    if text == '/logs':
        if await is_owner(update, 'logs check'):
            await send_log(bot, update)
            return

    if text == '/users':
        if await is_owner(update, 'users check'):
            await send_users(bot, update)
            return

    if text.startswith('/add'):
        if await is_owner(update, 'add user'):
            await add_user(update)
            return

    if text == '/clearusers':
        if await is_owner(update, 'clear user'):
            await clear_users(bot)
            return

    if text == '/sendusermsg':
        if await is_owner(update, 'check features'):
            await send_users_msg(bot, update)

    if text == '/featuresend':
        if await is_owner(update, 'check features'):
            await send_feature(bot, update)
            return

    if text == '/send':
        if await is_owner(update, 'check send'):
            await send(bot, update)
            return

    if text == '/news':
        if await is_owner(update,'ask multiple news'):
            await hiru_main(bot, update)
        sleep(15)
        await news_first_main(bot, update)
        sleep(15)
        await gagana_main(bot, update)
        sleep(15)
        await neth_main(bot, update)
        sleep(15)
        await rata_main(bot, update)
        sleep(15)
        await sinhala_news_main(bot, update)
        sleep(15)
        await ceynewfac_main(bot, update)
        sleep(15)
        await colombotimes_main(bot, update)
        sleep(15)
        await lankacnews_main(bot, update)
        sleep(15)

    if text == '/hirunews':
        await hiru_main(bot, update)
        return

    if text == '/newsfirst':
        await news_first_main(bot, update)
        return

    if text == '/gagana':
        await gagana_main(bot, update)
        return

    if text == '/neth':
        await neth_main(bot, update)
        return

    if text == '/rata':
        await rata_main(bot, update)
        return

    if text == '/sinhalanews':
        await sinhala_news_main(bot, update)
        return

    if text == '/ceyfac':
        await ceynewfac_main(bot, update)
        return

    if text == '/ctimes':
        await colombotimes_main(bot, update)
        return

    if text == '/lankacnews':
        await lankacnews_main(bot, update)
        return

    if text.startswith('https://www.hirunews.lk/'):
        await hiru_page(bot, update)
        return

    if text.startswith('https://www.newsfirst.lk/'):
        await news_first_page(bot, update)
        return

    if text.startswith('https://gagana.lk/'):
        await gagana_page(bot, update)
        return

    if text.startswith('http://nethnews.lk/'):
        await neth_page(bot, update)
        return

    if text.startswith('https://sinhala.news.lk/'):
        await update.reply_text("සමාවන්න. මෙය කලබාගැනීමට අපහසුය.")
        # await sinhala_news_page(bot, update)
        return

    if text.startswith('https://ceylonnewsfactory.com/'):
        await ceynewfac_page(bot, update)
        return

    if text.startswith('https://lankacnews.com/'):
        await lankacnews_page(bot, update)
        return

    if text.startswith('http://colombotimes.lk/'):
        await colombotime_page(bot, update)
        return

    if text.startswith('https://si.rata.lk/'):
        await rata_page(bot, update)
        return

    if text.startswith('/penpals'):
        await penpals_main(bot, update)
        return

    if text.startswith('/suggest'):
        await feature_suggest(update)
        return

    # TODO -> TO BE REANALYZE
    if text == 'xhams' or text == '/xhams_help':
        if await is_owner(update, 'xhams'):
            await xham_main(bot, update)
            return

    if text == 'xvid' or text == '/xvid_help':
        if await is_owner(update, 'xvid'):
            await xham_main(bot, update)
            return

    if 'xvideos.com/video' in text:
        if await is_owner(update, 'xvideo link'):
            await xvid_page_videos(bot, update)
            return

    if 'xsearch' in text:
        if await is_owner(update, 'xsearch'):
            await xvid_search(bot, update)
            return

    await update.reply_text("I don't know 🤥")
    await write_log(f'{update.chat.id} unknown {update.text}')
