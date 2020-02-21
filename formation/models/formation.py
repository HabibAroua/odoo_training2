from odoo import models , fields

class Registration(models.Model):
    _name='registration.registration'
    _description='registration.registration'

    name = fields.Char(string='nom', required=False , readonly=False)
    code = fields.Char(string='code', required=False, readonly=False)
    start_date = fields.Date("Date de debut" , help="Date")
    end_date = fields.Date("Date de fin", help="Date")
    #description = fields.Text(string='description', required=False, readonly=False)
    level_id= fields.Many2one('cycle.cycle',string="Cycle")
    year_id= fields.Many2one('year.year' , string ='annee unversitaire')
    claim_ids = fields.One2many('claim.claim','reg_ids' ,string='Reclamation')

class Claim(models.Model):
    _name='claim.claim'
    _description='Reclamation'

    name = fields.Char(string='nom', required=False , readonly=False)
    code = fields.Char(string='code', required=False, readonly=False)
    start_date = fields.Date("Date de debut" , help="Date")
    end_date = fields.Date("Date de fin", help="Date")
    #description = fields.Text(string='description', required=False, readonly=False)
    reg_ids=fields.Many2one('registration.registration' , string="Inscription")

class Year(models.Model):
    _name='year.year'
    _description='year.year'

    name = fields.Char(string='nom', required=False , readonly=False)
    code = fields.Char(string='code', required=False, readonly=False)
    start_date = fields.Date("Date de debut" , help="Date")
    end_date = fields.Date("Date de fin", help="Date")
    #description = fields.Text(string='description', required=False, readonly=False)
    session_ids= fields.One2many('session.session','year_id',string='Session')

class Session(models.Model):
    _name='session.session'
    _description='session.session'

    name = fields.Char(string='nom', required=False , readonly=False)
    code = fields.Char(string='code', required=False, readonly=False)
    start_date = fields.Date("Date de debut" , help="Date")
    end_date = fields.Date("Date de fin", help="Date")
    #description = fields.Text(string='description', required=False, readonly=False)
    year_id=fields.Many2one('year.year',string='annee unversitaire')

class Cycle(models.Model):
    _name='cycle.cycle'
    _description='cycle.cycle'

    name = fields.Char(string='nom', required=False , readonly=False)
    code = fields.Char(string='code', required=False, readonly=False)
    #description = fields.Text(string='description', required=False, readonly=False)
    level_ids=fields.One2many('level.level','cycle_id',string="Niveau")


class Level(models.Model):
    _name='level.level'
    _description='level.level'

    name = fields.Char(string='nom', required=False , readonly=False)
    code = fields.Char(string='code', required=False, readonly=False)
    #description = fields.Text(string='description', required=False, readonly=False)
    section_ids=fields.One2many('section.section','level_id',string="Section")
    cycle_id = fields.Many2one('cycle.cycle', string="Cycle")

class Section(models.Model):
    _name='section.section'
    _description='section.section'

    name=fields.Char(string='Nom',required=False, readonly=False)
    code=fields.Char(string='code',required=False, readonly=False)
    #_description=fields.Text(string='Description',required=False, readonly=False)
    module_ids = fields.One2many("module.module",'section_id', string='Module' )
    level_id=fields.Many2one('level.level','Niveau')

class Module(models.Model):
    _name = 'module.module'
    _description = 'modules'

    name = fields.Char(string='code', required=True)
    code = fields.Char(string='code', default='001')
    #_description = fields.Text(string='Description')
    section_id=fields.Many2one("section.section", string='Module')