from odoo import models, fields, api

class DocumentHeritage(models.Model): #Toute les classes d'odoo herite de la classe prédéfinie Model € Odoo
    _inherit = 'biblio.livre'
    _sql_constraints = [
        ('id_unique',
         'UNIQUE(book_id)',
         "ID du livre doit etre unique"),
    ]
    pages_number = fields.Integer(string='Nombre de pages')

    @api.constrains('book_release_date')
    def _Verifier_date_sortie(self):
        for r in self:
            if r.book_release_date > fields.Date.today():
                raise models.ValidationError(
                    'La date de sortie doit etre dans le passe')

class InscriptionBiblio(models.Model):
     _name = 'biblioo.inscription'
     nom_utilisateur = fields.Many2one('res.users', string='Utilisateur Bibliotheque', )
     date_debut_inscription = fields.Date(string='Date inscription utilisateur')
     date_fin_inscription = fields.Date(string='Date fin inscription utilisateur')
     nombre_livres_lus = fields.Integer(string='Le nombre de livres lus par utilisateur')
     prix = fields.Float(string="Le prix en DT")
     prix_uniatire=fields.Float(string="Le prix unitaire")

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

    @api.onchange('total_number_of_books', 'number_of_books_out')
    def _books_logic_error(self):
        var =\
        {
            '':
            {
                'title': "",
                'message': "",
             },
        }
        if ((self.total_number_of_books < self.number_of_books_out)):
            var= \
            {
                'warning':
                 {
                    'title': "Erreur de saisie",
                    'message': "Le nombre total des livres de la bibliotheque doit etre supérieur au nombre de livres sortis",
                 },
            }
        elif((self.total_number_of_books<0 or self.number_of_books_out <0)):
            var = \
            {
                'warning':
                {
                    'title': 'Erreur de saisie',
                    'message' : 'Il y un champ '
                }
            }
        return var