from odoo import models, fields, api

class DocumentHeritage(models.Model):
    _inherit = 'biblio.livre'
    pages_number = fields.Integer(string='Nombre de pages')

class InscriptionBiblio(models.Model):
     _name = 'biblioo.inscription'
     nom_utilisateur = fields.Many2one('res.users', string='Utilisateur Bibliotheque', )
     date_debut_inscription = fields.Date(string='Date inscription utilisateur')
     date_fin_inscription = fields.Date(string='Date fin inscription utilisateur')
     nombre_livres_lus = fields.Integer(string='Le nombre de livres lus par utilisateur')
     prix = fields.Float(string="Le prix en DT")
