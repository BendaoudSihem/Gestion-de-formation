# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    
    'name': 'Gestion des formations',
    'version': '1.0',
    'category': 'formations',
    'author': 'Sihem',
    'depends': ['project'],
    'data': ['views/formation_views.xml',
            'wizard/wizard.xml',
            'security/access.xml',
            'security/ir.model.access.csv',
            'report/report.xml',
            'views/session_views.xml',
            'views/atestation_views.xml',
    		'views/formateur_views.xml'

    ],
    'sequence': '0',
    'description': 'Ce module est destine pour gérer un centre de formation',
   # 'application':true
   
  
    
}
