# -*- coding: utf-8 -*-
{
    'name': "Construction Site Management",
    'summary': "Construction Site Management",
    'description': "Description of Construction Site Management",
    'category': 'Uncategorized',
    'version': '0.1',
    "license": 'LGPL-3',

    'depends': ['base','stock', 'mail'],

    'data': [         
        'views/views.xml',
        'views/templates.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/chantier/chantier.xml',        
        'views/chantier/menu_chantier.xml',
        'views/emplacement/emplacement.xml',
        'views/emplacement/menu_emplacement.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'application': True ,
    'installable': True ,
    'auto_install': False,
    'sequence': 1,
    
}