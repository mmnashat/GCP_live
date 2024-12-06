# -*- coding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2023 Leap4Logic Solutions PVT LTD
#    Email : sales@leap4logic.com
#################################################


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class L4lBOMLinesFromProduct(models.TransientModel):
    _name = 'bom.lines.from.product'
    _description = 'BOM Lines from Product List'

    bom_id = fields.Many2one('mrp.bom', string="BOM")
    product_ids = fields.Many2many('product.product', string="Products")
    operation_type = fields.Selection([('add_new', 'Add as a new products'), ('replace_existing', 'Replace existing with products')],string="Operation Type", default='add_new')
    is_bom_opened = fields.Boolean(string="Is BOM Opened")

    def default_get(self, fields):
        res = super(L4lBOMLinesFromProduct, self).default_get(fields)
        if self.env.context.get('default_bom_id'):
            res['is_bom_opened'] = True
        return res

    def action_import(self):
        if not self.bom_id:
            raise ValidationError(_("Please select a bills of materials."))
        if not self.product_ids:
            raise ValidationError(_("Please select at least one product."))
        if self.operation_type == 'replace_existing':
            self.bom_id.bom_line_ids.unlink()
        for product in self.product_ids:
            self.env['mrp.bom.line'].create({
                'bom_id': self.bom_id.id,
                'product_id': product.id,
            })
        if not self.is_bom_opened:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Bill of Materials',
                'res_model': 'mrp.bom',
                'view_mode': 'form',
                'res_id': self.bom_id.id,
                'target': 'current',
            }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
