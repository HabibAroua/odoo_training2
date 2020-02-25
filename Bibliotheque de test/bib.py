from odoo import models, fields, api

class Document(models.Model):

     _name = 'biblio.livre' # le nom de table dans la base de donneé

     name = fields.Char(string="Titre", required=True)
     description = fields.Text()

     #author_name = fields.Char(string='NomAuteur', required=True)
     author_name = fields.Many2many('res.partner', string='Auteurs')
     book_id = fields.Integer(string='ID dulivre', required=True)
     book_release_date = fields.Date(string="Date sortiedulivre")
     is_bestseller = fields.Boolean('Bestseller?')
     book_genre = fields.Selection\
     (
               [
                    ('h', 'Horreur'),
                    ('s', 'Science'),
                    ('a', 'Aventure'),
                    ('r','Romance'),
                    ('p', 'Policier'),
                    ('au', 'Autre')
               ],
               'Genre dulivre'
     )
     publisher_id = fields.Many2one('res.partner', string='Editeur', )

     @api.constrains('book_release_date')
     def _Verifier_date_sortie(self):
          for r in self:
               if r.book_release_date > fields.Date.today():
                    raise models.ValidationError(
                         'La date de sortie doit etre dans le passe')

     @api.constrains('author_name')
     def _Verifier_author_name(self):
          for r in self:
               if self.author_name == '':
                    raise  models.ValidationError('Author est vide !!!!!')