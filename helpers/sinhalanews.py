import requests as req
from bs4 import BeautifulSoup as Soup

from helpers.common import write_log

URL = 'https://sinhala.news.lk/'
PREFIX = 'https://sinhala.news.lk'


async def sinhala_news_main(bot, update):
    await write_log(f'{update.chat.id} - SinhalaNews_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    news = soup.find_all('div', class_='nspArt nspCol3')

    for each_news in news:
        await bot.send_message(
            chat_id=update.chat.id,
            text=PREFIX + each_news.a['href']
        )


async def sinhala_news_page(bot, update):
    page_url = update.text

    await write_log(f'{update.chat.id} - SinhalaNews_Page - {page_url}')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    main = soup.find('div', class_='itemBody')

    paras = main.find_all('p')

    for p in paras:
        await bot.send_message(
            chat_id=update.chat.id,
            text=p.text
        )
