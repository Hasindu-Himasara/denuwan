import requests as req
from bs4 import BeautifulSoup as Soup
from helpers.common import write_log

URL = 'https://www.hirunews.lk/'


async def hiru_main(bot, update):
    await write_log(f'{update.chat.id} - HiruNews_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    main = soup.find('div', class_='main-article-section')

    head_news = soup.find('div', class_='main-article-topic').a['href']
    await bot.send_message(
        chat_id=update.chat.id,
        text=head_news
    )

    news = main.find_all('div', class_='row')

    for n in news:
        await bot.send_message(
            chat_id=update.chat.id,
            text=n.a['href']
        )


async def hiru_page(bot, update):
    URL = update.text

    await write_log(f'{update.chat.id} - HiruNews_Page - {URL}')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    main = soup.find('div', id='article-phara')

    para = main.text

    start = 0
    end = 1000
    parts = len(para) / 1000
    index = 0

    while index < parts:
        await bot.send_message(
            chat_id=update.chat.id,
            text=para[start:end]
        )
        start += 1000
        end += 1000
        index += 1
