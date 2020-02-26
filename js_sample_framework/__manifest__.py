{
    'name': "JS Framework",
    'version':'1.0',
    'author':'Habib Aroua',
    'website':'http://www.habib_aroua.com',
    'support':'habib.aroua@sesame.com.tn',
    'license':'AGPL-3',
    'complexity':'easy',
    'sequence':1,
    'summary': """first JS Framework""",

    'description': """
        this is my first odoo module using JS
    """,

    'category': 'JavaScript',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'view.xml',
        #'report.xml'
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'css' : [

    ],
    'price':100.00,
    'currency':'EUR',
    'installable' : True,
    'application' :True,
}