from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name= 'biblioo.wizard'

    Date_reinscription = fields.Date('Date reinscription')
    Date_finscription = fields.Date('Nouvelle date de fin inscription')

    @api.multi
    def action_reinscrire(self):
        nom_inscrit= self.env['biblioo.inscription'].browse(self._context.get('active_ids'))
        for name in nom_inscrit:
            name.date_debut_inscription = self.Date_reinscription
            name.date_fin_inscription = self.Date_finscription
            name.state = 'inscrit'