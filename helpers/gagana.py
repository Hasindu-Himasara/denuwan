import requests as req
from bs4 import BeautifulSoup as Soup
from helpers.common import write_log

URL = 'https://gagana.lk/'


async def gagana_main(bot, update):
    await write_log(f'{update.chat.id} - Gagana_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    # BREAKING NEWS
    breaking = soup.find('div', class_='breaking-article-section')
    await bot.send_message(
        chat_id=update.chat.id,
        text=breaking.a['href']
    )

    # Top 2 Article
    top2_conrainer = soup.find('div', class_='top-article-section')
    top2 = top2_conrainer.find_all('div', class_='col-lg-6 col-md-6 col-12')

    for each_top in top2:
        await bot.send_message(
            chat_id=update.chat.id,
            text=each_top.a['href']
        )

    container = soup.find('div', class_='lsba-sec')

    news = container.find_all('div', class_='a-item')

    for each_news in news:
        await bot.send_message(
            chat_id=update.chat.id,
            text=each_news.a['href']
        )


async def gagana_page(bot, update):
    URL = update.text

    await write_log(f'{update.chat.id} - Gagana_Page - {URL}')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    main = soup.find('div', class_='ds-content')

    paras = main.find_all('p')

    temp = ''
    for p in paras:
        if p.text == '':
            continue
        if len(temp) + len(p.text) < 1000:
            temp += '\n' + p.text
            continue

        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
        temp = p.text

    if temp != '':
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )
