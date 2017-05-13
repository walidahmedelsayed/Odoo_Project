from odoo import models , fields
from lxml import html
import requests

class Product(models.Model):

    _name = 'project.products'

    product_url = fields.Text(string="Product URL") 
    name = fields.Char(string='Product')
    # category = fields.Char(string='Category')
    price = fields.Float(string='Price')
    image = fields.Text()
    description = fields.Text(string='Description')


  