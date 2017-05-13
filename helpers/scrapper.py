from lxml import html
import requests

class OSOdooScrapper:

	def __init__(self, page_url):

		self.page = requests.get(page_url)
		# page = requests.get('https://egypt.souq.com/eg-en/samsung-galaxy-j1-mini-prime-dual-sim-8gb-1gb-ram-3g-black-11711148/i/')
		self.tree = html.fromstring(self.page.content)

	def get_title(self):
		title = self.tree.xpath('//*[@id="offer_active"]/div[2]/div[1]/div[1]/div[1]/h1/text()')[0].strip()
		return title
	
	def get_price(self):
		price = self.tree.xpath('//*[@id="offeractions"]/div[1]/div[1]/strong/text()')[0].strip()
		return price

	# def get_category(self):
	# 	category = self.tree.xpath('//*[@id="breadcrumbTop"]/tbody/tr/td[2]/ul/li[2]/a/span/text()')[0].strip()
	# 	return category

	def get_description(self):
		description = self.tree.xpath('//*[@id="textContent"]/p/text()')[0].strip()
		return description

	def get_image_url(self):
		imageURL = self.tree.xpath('//*[@id="offerdescription"]/div[1]/div/div/div/div/img')[0].get('src')
		return imageURL

# scrapper = OSOdooScrapper('https://olx.com.eg/ad/5-ID7HD6Z.html')

# print('title is ' + scrapper.get_title())
# print('price is ' + scrapper.get_price())
# print('image is ' + scrapper.get_image_url())
# print('desc is ' + scrapper.get_description())
