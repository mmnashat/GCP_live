# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2024 ZestyBeanz Technologies(<http://www.zbeanztech.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Manufacturing Order Material Request',
    'version': '17.0.0.0.1',
    'category': 'Manufacturing',
    'summary': " This module helps to create an Internal Transfer request for the components required for completing the Manufacturing Order.",
    'website': 'https://www.zbeanztech.com',
    'description': """
     This module helps to create an Internal Transfer request for the components required for completing the Manufacturing Order...
        """,
    'author': 'ZestyBeanz Technologies',
    'maintainer': 'ZestyBeanz Technologies',
    'support': 'support@zbeanztech.com',
    'license': 'LGPL-3',
    'icon': "/zb_mo_component_request/static/description/icon.png",
    'images': ['static/description/banners/banner.png',],
    'currency': 'USD',
    'price': 0.0,
    'depends': ['mrp'],
    'data': [
            'views/mrp_production_view.xml',
            'views/stock_picking_view.xml',
            
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

