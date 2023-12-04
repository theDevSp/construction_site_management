# -*- coding: utf-8 -*-
{
    'name': "Gestion Chantiers",
    'summary': "Gestion Chantier",
    'description': "Ce Module permet la gestion des chantiers, les équipes travaillant sur un chantier, affectation des citerne, affectation des engin ...",
    'category': 'Uncategorized',
    'version': '0.1',
    "license": 'LGPL-3',

    'depends': [
        'base',
        'stock',
        'mail',
        'configuration_module'
    ],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/chantier/chantier.xml',
        'views/emplacement/emplacement.xml',
        'views/responsable/responsable_chantier_view.xml',

        'views/chantier/menu_chantier.xml',
        'views/chantier/sequence_chantier.xml',
        'views/emplacement/menu_emplacement.xml',
        'views/config/config_menu.xml',
        'views/responsable/responsable_chantier_menu.xml',
        'views/res_users/res_users.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'construction_site_management/static/src/js/*.js',
            'construction_site_management/static/src/js/**/**/*.js',
            'construction_site_management/static/src/xml/*.xml',
            'construction_site_management/static/src/xml/**/*.xml',
            'construction_site_management/static/src/xml/**/**/*.xml',
            'construction_site_management/static/src/css/*.scss',
        ],
        'web.assets_common': [
            'construction_site_management/static/src/**/*.scss',
        ],

    },

    'application': True,
    'installable': True,
    'auto_install': False,
    'sequence': 11,

}
