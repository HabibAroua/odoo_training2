{
    'name': "Exemple de bibiotheque",
    'version':'1.0',
    'author':'Habib Aroua Sesame',
    'website':'http://www.habib_aroua.com',
    'support':'habib.aroua@sesame.com.tn',
    'license':'AGPL-3',
    'complexity':'easy',
    'sequence':1,
    'summary': """Bib""",

    'description': """
        Habib dev Odoo
        module1
        module2
        module3
    """,

    'category': 'Formation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'view.xml',
        #'views/templates.xml',
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