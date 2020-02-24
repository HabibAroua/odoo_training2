from odoo import models, fields, api

class DocumentHeritage(models.Model):
    _inherit = 'biblio.livre'
    pages_number = fields.Integer(string='Nombre de pages')