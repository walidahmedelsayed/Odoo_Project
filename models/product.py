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
        # objs = self.pool.get('project.products')
        records = self.env['project.products'].search([])
        print ("all", records)
        for record in records:
            print ("id :", record.id)
            obj = self.env['project.products'].browse([record.id])
            scrapper = OSOdooScrapper(obj.url)
            title = scrapper.get_title()
            category = scrapper.get_category()
            price = scrapper.get_price()
            # description = scrapper.get_description()
            updates = obj.numberOfUpdates
            print ("current num :", updates)
            res = obj.write({"title": title, "category": category, "price": price,
                             "numberOfUpdates": updates + 1})
            print ("status :", res)

    def get_data(self):
        myScrapper = OSOdooScrapper(self.url)
        self.title = myScrapper.get_title()
        self.category = myScrapper.get_category()
        self.price = myScrapper.get_price()
        self.numberOfUpdates += 1
        self.description = myScrapper.get_description()





