import requests as req
from bs4 import BeautifulSoup as Soup

from helpers.common import write_log

URL = 'http://nethnews.lk/'


async def neth_main(bot, update):
    await write_log(f'{update.chat.id} - Neth_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    top_news = soup.find('div', class_='top_breaking_news_content')
    print(top_news.a['href'])

    news = soup.find_all('div', class_='breaking_news breaknew')

    for each_news in news:
        await bot.send_message(
            chat_id=update.chat.id,
            text=each_news.a['href']
        )


async def neth_page(bot, update):
    URL = update.text

    await write_log(f'{update.chat.id} - Neth_Page - {URL}')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    #################
    header = soup.find('div', class_='td-post-header').text
    #################

    paras = soup.find_all('div', class_='td-post-content')

    temp = f'<b>{header}</b>'
    for para in paras:
        txt = para.text
        if len(temp) + len(txt) < 1000:
            temp += '\n' + txt
            continue

        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
        temp = txt
    if temp != '':
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
