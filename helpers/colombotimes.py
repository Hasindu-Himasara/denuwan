import requests as req
from bs4 import BeautifulSoup as Soup
from helpers.common import write_log

URL = 'http://colombotimes.lk/'


async def colombotimes_main(bot, update):
    await write_log(f'{update.chat.id} - ColomboTimes_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    container = soup.find('div', class_='loop-container')
    news = container.find_all('div')

    for each_news in news:

        try:
            news_text = each_news.find('article').text
        except:
            continue
        if news_text is None:
            continue
        try:
            news_link = each_news.a['href']

        except:
            continue

        await bot.send_message(
            chat_id=update.chat.id,
            text=news_link
        )


async def colombotime_page(bot, update):
    url = update.text

    await write_log(f'{update.chat.id} - ColomboTimes_Page - {url}')

    r = req.get(url)
    soup = Soup(r.content, 'html5lib')
    news = soup.find_all('p')
    index = len(news)

    temp = ''
    for i in range(1, index - 1):

        if len(temp) + len(news[i].text) < 1000:
            temp += '\n' + news[i].text
            continue
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
        temp = news[i].text

    if temp != '':
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
