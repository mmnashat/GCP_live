# -*- coding: utf-8 -*-
# Copyright 2024 RL Software Development ApS. See LICENSE file for full copyright and licensing details.
{
    'name': "Stock - select move date",

    'summary': """

        Adds the possibility to select the date of the move when creating a stock move in field 'Date of transport'
    
    """,

    'description': """
        
    """,
    'author': "RL Software Development ApS",
    'website': "https://www.rlsd.dk/",
    'category': 'Inventory',
    'version': '17.0.1.0.3',
    'depends': [
        'stock_account', 
        'stock', 
    ],
    'data': [
        'views/stock_picking.xml',
        'views/stock_valuation_layer.xml',
        
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
}