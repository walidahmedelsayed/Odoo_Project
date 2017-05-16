from lxml import html
import requests


class OSOdooScrapper:
    def __init__(self, page_url):
        self.page = requests.get(page_url)
        # page = requests.get('https://egypt.souq.com/eg-en/samsung-galaxy-j1-mini-prime-dual-sim-8gb-1gb-ram-3g-black-11711148/i/')
        self.tree = html.fromstring(self.page.content)

    def get_title(self):
        title = self.tree.xpath('//*[@id="content-body"]/div/header/div[2]/div[2]/div/div[1]/div[1]/div/h1/text()')[
            0].strip()
        return title

    def get_price(self):
        price = \
        self.tree.xpath('//*[@id="content-body"]/div/header/div[2]/div[2]/div/div[2]/div/section/div/h3/text()')[
            1].strip()
        return price

    def get_category(self):
        category = \
        self.tree.xpath('//*[@id="content-body"]/div/header/div[2]/div[2]/div/div[1]/div[1]/div/span[1]/a[2]/text()')[
            0].strip()
        return category

    def get_description(self):
        description = self.tree.xpath('//*[@id="description-full"]/div/div[1]/div/p/text()')[0].strip()
        return description


scrapper = OSOdooScrapper(
    'https://egypt.souq.com/eg-en/samsung-galaxy-j1-mini-prime-dual-sim-8gb-1gb-ram-3g-black-11711148/i/')

print(scrapper.get_price())
