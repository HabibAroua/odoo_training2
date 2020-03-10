from odoo import fields, models, api
from odoo.exceptions import UserError

class Customer(models.Model):
    _name = 'nursery.customer'

    name=fields.Char('Customer Name' , required=True)
    email = fields.Char(help = 'To receive the newsletters')