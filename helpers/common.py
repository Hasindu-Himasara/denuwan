from datetime import datetime
import os
import pytz
from time import sleep

AUTHORIZED = []

AUTH_PATH = 'helpers/auth.txt'
LOG_PATH = 'helpers/log.txt'
FEATURE_PATH = 'helpers/suggest.txt'

OWNER_ID = 844127137


async def send_users_msg(bot, update):
    txt = update.text.split('/sendusermsg')
    if len(txt) == 1:
        await update.reply_text("Incorrect Msg!😒")
        return

    msg = txt[1]
    f = open(AUTH_PATH, 'r')
    temp = []

    for temp_id in f:
        if temp_id in temp:
            continue
        temp.append(int(temp_id.strip()))

    for temp_id in temp:
        await bot.send_message(
            chat_id=update.chat.id,
            reply_to_message_id=temp_id,
            text=msg
        )
        sleep(10)

    await write_log(f'{update.chat.id} send msg to all {msg}')


async def is_user(update):
    user_id = update.chat.id

    return user_id in AUTHORIZED or user_id == OWNER_ID


async def is_sudo(update):
    user_id = update.chat.id

    if user_id == OWNER_ID:
        return True

    return False


ADD_USER_HINT = '<b>Hint : </b> <code>/auth 12345 67890</code>'


async def add_user(update):
    if not await is_sudo(update):
        await update.reply_text("You're not the Owner!😹")

        await write_log(f'{update.chat.id} tried to add users {update.text}')

        return

    if ' ' not in update.text:
        await update.reply_text(ADD_USER_HINT)
        return

    if not os.path.isfile(AUTH_PATH):
        with open(AUTH_PATH, 'w') as f:
            AUTHORIZED.append(OWNER_ID)
            f.write(str(OWNER_ID))
        f.close()

    words = update.text.split(' ')

    f = open(AUTH_PATH, 'a')

    for user_id in range(1, len(words)):
        try:
            temp = int(user_id.strip())
        except:
            await update.reply_text('Error input!😒')
            f.close()
            return

        if temp in AUTHORIZED:
            continue

        f.write('\n' + str(temp))
        AUTHORIZED.append(temp)

        await write_log(f'Authoried {temp}')

    f.close()


async def clear_users(update):
    global AUTHORIZED

    if not await is_sudo(update):
        await update.reply_text("You're not the Owner!😹")

        await write_log(f'{update.chat.id} tried to add users {update.text}')

        return

    with open(AUTH_PATH, 'w') as f:
        f.write(str(OWNER_ID))

    AUTHORIZED = [OWNER_ID]

    await write_log('Authorized cleared!')


async def send_log(bot, update):
    if not await is_sudo(update):
        await update.reply_text("You're not the Owner!😹")
        await write_log(f'{update.chat.id} tried to send logs')
        return

    else:
        await bot.send_document(
            chat_id=update.chat.id,
            document=LOG_PATH,
            caption='Logs'
        )


async def send_users(bot, update):
    if not await is_sudo(update):

        await update.reply_text("You're not the Owner!😹")
        await write_log(f'{update.chat.id} tried to send users')
        return

    else:
        if not os.path.isfile(AUTH_PATH):
            with open(AUTH_PATH,'w') as f:
                f.write(str(OWNER_ID))
            f.close()
        await bot.send_document(
            chat_id=update.chat.id,
            document=AUTH_PATH,
            caption='Authorized'
        )


async def get_now():
    asia = pytz.timezone('Asia/Kolkata')

    asian_time = datetime.now(asia)
    date_time = asian_time.strftime('%Y:%m:%d %H:%M:%S')

    return date_time


async def write_log(description):
    if not os.path.isfile(LOG_PATH):
        with open(LOG_PATH, 'w') as f:
            f.write(await get_now() + ' - Log Started')

        f.close()

    with open(LOG_PATH, 'a') as f:
        f.write('\n' + await get_now() + ' - ' + description)

    f.close()


async def feature_suggest(update):
    text = update.text.split('/suggest')

    if len(text) == 1 or text[1].strip() == '':
        await update.reply_text("<b>Give Me Suggests !!!🤬</b>")
        return

    if not os.path.isfile(FEATURE_PATH):
        with open(FEATURE_PATH, 'w') as f:
            f.write('Features\n' + str(update.chat.id) + ' - ' + text[1])
        f.close()
        await write_log(f'{update.chat.id} added suggest')
        return

    with open(FEATURE_PATH, 'a') as f:
        f.write('\n' + str(update.chat.id) + ' - ' + text[1])

    f.close()
    await write_log(f'{update.chat.id} added suggest')
    await update.reply_text("<b>Thank For Your Suggests 💝</b>")


async def send_feature(bot, update):
    if not await is_sudo(update):

        await update.reply_text("You're not the Owner!😹")
        await write_log(f'{update.chat.id} tried to read features')
        return

    else:
        if not os.path.isfile(FEATURE_PATH):
            with open(FEATURE_PATH,'w')as f:
                f.write("Features")
                f.close()
        await bot.send_document(
            chat_id=update.chat.id,
            document=FEATURE_PATH,
            caption='Features'
        )
