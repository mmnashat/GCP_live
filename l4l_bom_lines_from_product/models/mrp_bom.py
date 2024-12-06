# -*- coding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2023 Leap4Logic Solutions PVT LTD
#    Email : sales@leap4logic.com
#################################################


from odoo import _, api, fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    def button_add_components(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Components Wizard',
            'res_model': 'bom.lines.from.product',
            'view_mode': 'form',
            'view_id': self.env.ref('l4l_bom_lines_from_product.view_bom_lines_from_product_wizard').id,
            'target': 'new',
            'context': {'default_bom_id': self.id, }
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
