from odoo import models, fields
from lxml import html
import requests


class Product(models.Model):
    _name = 'project.products'
    url = fields.Char(string='product url')
    name = fields.Char(string='Product')
    category = fields.Char(string='Category')
    price = fields.Float(string='Price')
    image = fields.Binary()



    # page = requests.get('https://deals.souq.com/eg-en?a_source=google&a_medium=cpc&a_content=search_brand&a_term=souq&u_type=text&u_mt=e&u_title=A_Souq_EX&a_campaign=SN-EG-EN-Brand&gclid=CJizqJTF49MCFQWVGwodTvUB0Q')
    # tree = html.fromstring(page.content)
    # details = tree.xpath('//div/img/@src')
    #
    #
    # print (details)
