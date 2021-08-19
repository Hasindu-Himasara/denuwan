import requests as req
from bs4 import BeautifulSoup as Soup

from helpers.common import write_log

URL = 'https://si.rata.lk/category/%e0%b6%b4%e0%b7%94%e0%b7%80%e0%b6%ad%e0%b7%8a/'


async def rata_main(bot, update):
    await write_log(f'{update.chat.id} - Rata_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')
    news = soup.find_all('div', class_='tdb_module_loop td_module_wrap td-animation-stack')

    for each_news in news:
        link = each_news.find_all('a')[-1]['href']

        await bot.send_message(
            chat_id=update.chat.id,
            reply_to_message_id=update.message_id,
            text=link
        )


async def rata_page(bot, update):
    url = update.text

    await write_log(f'{update.chat.id} - Rata.lk_Page - {url}')

    r = req.get(url)
    soup = Soup(r.content, 'html5lib')
    paras_position = soup.find_all('div', class_='tdb-block-inner td-fix-index')[13]
    paragraphs = paras_position.find_all('p')

    temp = ''
    for para in paragraphs:
        if len(temp) + len(para.text) < 1000:
            temp += '\n' + para.text
            continue

        await bot.send_message(
            chat_id=update.chat.id,
            text=para.text
        )
        temp = para.text

    if temp != '':
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
