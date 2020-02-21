from odoo import models, fields, api

class Document(models.Model):
     _name = 'biblioth.livre'
     name = fields.Char(string="Titre", required=True)
     description = fields.Text()
     author_name = fields.Char(string='NomAuteur', required=True)
     book_id = fields.Integer(string='ID dulivre', required=True)
     book_release_date = fields.Date(string="Date sortiedulivre")
     is_bestseller = fields.Boolean('Bestseller?')
     book_genre = fields.Selection([('h', 'Horreur'), ('s', 'Science'), ('a', 'Aventure'), ('r','Romance'), ('p', 'Policier'), ('au', 'Autre')],'Genre dulivre')