import requests as req
from bs4 import BeautifulSoup as Soup
from helpers.common import write_log


URL = 'https://ceylonnewsfactory.com/'


async def ceynewfac_page(bot, update):
    url = update.text

    await write_log(f'{update.chat.id} - Ceylonnewsfactory_Page - {url}')

    r = req.get(url)
    soup = Soup(r.content, )
    rows = soup.find('article', class_='post-details')
    paras = rows.find_all('p')

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
        temp = para.text

    await bot.send_message(
        chat_id=update.chat.id,
        text=temp
    )

    temp = ''
    if 'blockquote' in r.text:
        block = soup.find('blockquote', class_='wp-block-quote')
        block_text = block.text

        await bot.send_message(
            chat_id=update.chat.id,
            text="Block_Quote - "
        )

        parts = len(block_text) / 1000
        start = 0
        end = 1000
        index = 0

        while index < parts:
            await bot.send_message(
                chat_id=update.chat.id,
                text=block_text[start:end]
            )
            start += 1000
            end += 1000
            index += 1

    if temp != '':
        await bot.send_message(
            chat_id=update.chat.id,
            text=temp
        )


async def ceynewfac_main(bot, update):
    await write_log(f'{update.chat.id} - CeylonNewsFactory_Main')

    r = req.get(URL)
    soup = Soup(r.content, 'html5lib')

    news = soup.find_all('div', class_='col-lg-6 col-md-6 col-sm-12')

    for each_news in news:
        news_link = each_news.a['href']
        await bot.send_message(
            chat_id=update.chat.id,
            text=news_link
        )
