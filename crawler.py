import asyncio
import re

import aiohttp
import bs4
from typing import TypeAlias

T_URL: TypeAlias = str
T_URLS: TypeAlias = list[T_URL]
T_HTML_TEXT: TypeAlias = str


async def get_text_from_url(url: T_URL) -> T_HTML_TEXT:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def get_urls(text: T_HTML_TEXT) -> T_URLS:
    soup = bs4.BeautifulSoup(markup=text, features='html.parser')
    urls = []
    for link_element in soup.find_all('a'):
        url = link_element.get('href')
        if re.match('https://ithillel.ua', str(url)):
            urls.append(url)
    return urls


def set_number_of_links() -> int:
    while True:
        try:
            number_of_links = int(input("Enter number of links: "))
        except ValueError:
            print("ERROR! Repeat")
            continue
        else:
            return number_of_links


async def main():
    number_of_links = set_number_of_links()

    with open("links.txt", "r") as file:
        count = 0
        urls = file.read().split('\n')
        for url in urls:
            text = await get_text_from_url(url=url)
            new_links = get_urls(text=text)
            for new_link in new_links:
                if new_link not in urls and count < number_of_links:
                    urls.append(new_link)
                    count += 1

    print('Saving to file "links.txt"')
    with open("links.txt", "w") as file:
        for url in urls:
            file.write(url + '\n')


if __name__ == '__main__':
    asyncio.run(main())
