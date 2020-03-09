from odoo import fields, models, api
from odoo.exceptions import UserError

class Order(models.Model):
    _name = 'nursery.order'

    name = fields.Datetime(default=fields.Datetime.now)
    plant_id = fields.Many2one("nursery.plant", required=True)
    customer_id = fields.Many2one("nursery.customer")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Canceled')
    ], default='draft')
    last_modification = fields.Datetime(readonly=True)

    def write(self, values):
        # helper to "YYYY-MM-DD"
        values['last_modification'] = fields.Datetime.now()

        return super(Order, self).write(values)

    def unlink(self):
        # self is a recordset
        for order in self:
           if order.state == 'confirm':
            raise UserError("You can not delete confirmed orders")

        return super(Order, self).unlink()

class Plants(models.Model):
    _name = 'nursery.plant'

    name = fields.Char("Plant Name")
    price = fields.Float()
    order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")
    order_count = fields.Integer(compute='_get_total_sold',store=True,string="Total sold")
    number_in_stock = fields.Integer()

    @api.depends('order_ids')
    def _get_total_sold(self):
        for plant in self:
            plant.order_count = len(plant.order_ids)

    @api.constrains('order_count', 'number_in_stock')
    def _check_available_in_stock(self):
        for plant in self:
            if plant.number_in_stock and \
              plant.order_count > plant.number_in_stock:
                raise UserError("There is only %s %s in stock but %s were sold"
                      % (plant.number_in_stock, plant.name, plant.order_count))


class Customer(models.Model):
    _name = 'nursery.customer'

    name=fields.Char('Customer Name' , required=True)
    email = fields.Char(help = 'To receive the newsletters')