# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) 2020 AtharvERP (<http://atharverp.com/>). All Rights Reserved
# Odoo Proprietary License v1.0
#
# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, atharverp.com or you have written agreement from
# author of this software owner.
#
# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
##############################################################################

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    cost_center_id = fields.Many2one("cost.center", string='Cost Center')

    # @api.model
    # def default_get(self, fields):
    #     result = super(AccountInvoice, self).default_get(fields)
    #     if result.get('purchase_id'):
    #         po_id = result.get('purchase_id')
    #         purchase_order = self.env['purchase.order'].browse(po_id)
    #         result.update(
    #             {'cost_center_id': purchase_order.cost_center_id and purchase_order.cost_center_id.id or False})
    #     return result

    @api.onchange('cost_center_id')
    def set_cost_center(self):
        for line in self.invoice_line_ids:
            line.cost_center_id = self.cost_center_id.id


class AccountInvoiceLine(models.Model):

    _inherit = 'account.move.line'

    cost_center_id = fields.Many2one("cost.center", string="Cost Center")

    # purchase_line_id = fields.Many2one(
    #     'purchase.order.line', 'Purchase Order Line', ondelete='set null', index=True)

    @api.onchange('quantity')
    def set_default_cost_center(self):
        if self.move_id.cost_center_id:
            self.cost_center_id = self.move_id.cost_center_id.id
