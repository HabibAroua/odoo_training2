from odoo import models, fields, api
from __future__ import division

class LibrairieGeneral(models.Model):
    _name = 'biblioo.general'
    total_number_of_books = fields.Integer(string='nombre total des livres', required=True)
    number_of_books_out = fields.Integer(string='nombre de livres sortis',required=True)
    date_situation = fields.Date(string='Date de la situation de la bibliotheque')
    taken_books_percentage = fields.Float(string="Pourcentage de livres sortis",compute='_taken_books')

    @api.depends('number_of_books_out','total_number_of_books')
    def _taken_books(self):
        self.taken_books_percentage=self.number_of_books_out/self.total_number_of_books*100\
            if self.total_number_of_books!= 0 else 0