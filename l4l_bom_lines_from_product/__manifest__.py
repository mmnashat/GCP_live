# -*- coding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2023 Leap4Logic Solutions PVT LTD
#    Email : sales@leap4logic.com
#################################################

{
    'name': "Bom Lines From Product",
    'category': 'Manufacturing',
    'version': '17.0.1.0',
    'sequence': 1,
    'summary': """Bom Lines From Product, Bills Of Materials, Add Components, Products, Product variants, Bom, Mrp bom, Lines, Operation Type, Bom Wizard, Bom lines, Multiple products, Import bom components, Manufacturing resource planning, Add as a new products, Replace existing with products, L4l, Leap, 4, Logic, Leap4logic""",
    'description': """This module helps you easily manage BOM (Bill of Materials) components. You can add or replace BOM component items using an easy-to-use interface. It simplifies updating your BOMs by allowing you to quickly add new products or update existing ones.""",
    'author': 'Leap4Logic Solutions Private Limited',
    'website': 'https://leap4logic.com/',
    'depends': ['mrp', 'stock', 'mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views_mrp_bom.xml',
        'wizard/wizard_bom_lines_from_product.xml',
    ],
    'application': True,
    'installation': True,
    'license': 'OPL-1',
    'images': ['static/description/banner.gif'],
    'price': '0.0',
    'currency': 'USD',
    'live_test_url': 'https://youtu.be/jgoG7R6j5dg',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
