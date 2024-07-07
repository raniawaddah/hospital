# -*- coding: utf-8 -*-
{
    'name': "Hospital System Odoo15",

    'summary': """
       Odoo 15
    """,

    'description': """
        Odoo15 Description
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/person.xml',
        'views/doctor.xml',
        'views/reservation.xml',
        'reports/person_report.xml',
        'views/sale_order.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
