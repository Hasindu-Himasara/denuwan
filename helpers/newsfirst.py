import requests as req
from bs4 import BeautifulSoup as Soup
from helpers.common import write_log

URL = 'https://www.newsfirst.lk/sinhala/latest-news/'


async def news_first_main(bot, update):
    await write_log(f'{update.chat.id} - NewsFirst_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    sections = soup.find_all('div', class_='col-md-12 news-lf-section')

    for sec in sections:

        main_news = sec.find('div', class_='col-md-5 fa-stack-w desktop-news-block-ppd no-padding-xs')
        await bot.send_message(
            chat_id=update.chat.id,
            text=main_news.a['href']
        )

        news_all = sec.find_all('div', class_='col-md-4 fb-stack-w desktop-news-block-ppd hidden-xs hidden-sm')

        for each_news in news_all:
            await bot.send_message(
                chat_id=update.chat.id,
                text=each_news.a['href']
            )


async def news_first_page(bot, update):
    url = update.text

    await write_log(f'{update.chat.id} - NewsFirst_Page - {url}')

    r = req.get(url)
    soup = Soup(r.content, 'html5lib')

    sec = soup.find('div', class_='text-left w-300 editor-styles')

    ########################
    news_header = sec.h3.text
    ########################

    temp = f'<b>{news_header}</b>'
    paras = sec.find_all('p')

    for p in paras:
        txt = p.text
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
