{
    'name' :'Plant Nursery',
    'version' : '1.0',
    'category' : 'Tools',
    'summary' : 'Plants and customers management',
    'depends' : ['web'],
    'data' : [
        #'security/ir/model.access.csv',
        #'data/data.xml',
        #'views.xml',
        #'complex.xml',
        'actions.xml',
        'orders_views.xml',
        'plants_views.xml',
    ],
    'demo': [
        #'data/demo.xml',
    ],
    'css' : [],
    'installable' : True,
    'auto-install' : False,
    'application': True,
}