import requests as req
from bs4 import BeautifulSoup as Soup

from helpers.common import write_log

URL = 'https://lankacnews.com/news/'


async def lankacnews_page(bot, update):
    url = update.text

    await write_log(f'{update.chat.id} - LankaCNews_Page - {url}')

    r = req.get(url)
    soup = Soup(r.content, 'html5lib')

    news = soup.find('article', class_='col-lg-12 col-md-12 news-item main-news main-news-item')
    paras = news.find_all('p')

    temp = ''
    for para in paras:
        para_text = para.text

        if len(temp) + len(para_text) < 1000:
            temp += '\n' + para_text
            continue

        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )

        temp = para_text

    if temp != '':
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )


async def lankacnews_main(bot, update):
    await write_log(f'{update.chat.id} - LankaCNews_Main')
    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    news = soup.find_all('article',
                         class_='col-lg-6 col-md-12 news-item main-news main-news-item cat-view-news-item clearfix')

    for each_news in news:
        news_link = each_news.a['href']

        await bot.send_message(
            chat_id=update.chat.id,
            reply_to_message_id=update.message_id,
            text=news_link
        )
