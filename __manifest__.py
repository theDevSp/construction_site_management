# -*- coding: utf-8 -*-
{
    'name': "Construction Site Management",
    'summary': "Construction Site Management",
    'description': "Description of Construction Site Management",
    #'author': "My Company",
    #'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock', 'mail'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/chantier.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True ,
    'installable': True ,
    'auto_install': False,
    'sequence': 1,
    
}