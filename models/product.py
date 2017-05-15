from odoo import models, fields
from lxml import html
import requests
from scrapper import OSOdooScrapper


class Product(models.Model):
    _name = 'project.products'
    url = fields.Char(string='product url')
    name = fields.Char(string='Product')
    category = fields.Char(string='Category')
    description = fields.Char(string='Description')
    title = fields.Char(string='Title')
    price = fields.Float(string='Price')
    image = fields.Binary()
    numberOfUpdates = fields.Integer('Number of updates')

    def automated_function(self):
        myScrapper = OSOdooScrapper(self.url)
        self.title = myScrapper.get_title()
        self.category = myScrapper.get_category()
        self.price = myScrapper.get_price()
        self.numberOfUpdates += 1



    # page = requests.get('https://deals.souq.com/eg-en?a_source=google&a_medium=cpc&a_content=search_brand&a_term=souq&u_type=text&u_mt=e&u_title=A_Souq_EX&a_campaign=SN-EG-EN-Brand&gclid=CJizqJTF49MCFQWVGwodTvUB0Q')
    # tree = html.fromstring(page.content)
    # details = tree.xpath('//div/img/@src')
    #
    #
    # print (details)
