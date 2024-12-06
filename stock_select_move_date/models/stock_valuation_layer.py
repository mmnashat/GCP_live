# -*- coding: utf-8 -*-

from odoo import fields, models, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class StockValuationLayerInherit(models.Model):
    _inherit = 'stock.valuation.layer'
    
    account_move_date = fields.Date(string='Accounting Date', related="account_move_id.date")
    
    #From stock_account / stock.valuation.layer
    # def _validate_accounting_entries(self):
    #     am_vals = []
    #     for svl in self:
    #         if not svl.with_company(svl.company_id).product_id.valuation == 'real_time':
    #             continue
    #         if svl.currency_id.is_zero(svl.value):
    #             continue

    #         move = svl.stock_move_id
    #         if not move:
    #             move = svl.stock_valuation_layer_id.stock_move_id
    #         am_vals += move.with_company(svl.company_id)._account_entry_move(svl.quantity, svl.description, svl.id, svl.value)
        
    #     if am_vals:
    #         account_moves = self.env['account.move'].sudo().create(am_vals)
    #         #Changed below to force post
    #         #account_moves._post()
    #         future_moves = account_moves.filtered(lambda move: move.date + relativedelta(days =- 62)  > fields.Date.context_today(self))

    #         if len(future_moves) == 0:                
    #             account_moves._post(soft=False)

    #         else:
    #             raise UserError(_("Can't post more than 62 days in to the future!\n\nPlease correct the date of transport. Or contact your system administrator."))

    #     for svl in self:
    #         # Eventually reconcile together the invoice and valuation accounting entries on the stock interim accounts
    #         if svl.company_id.anglo_saxon_accounting:
    #             svl.stock_move_id._get_related_invoices()._stock_account_anglo_saxon_reconcile_valuation(product=svl.product_id)   