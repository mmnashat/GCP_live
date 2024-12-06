# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError
from dateutil.relativedelta import relativedelta

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    
    date_of_transport = fields.Date(
        string='Date of transport', 
        readonly=False,
        copy=False
    )

    def write(self, vals):

        if 'date_done' in vals and 'priority' in vals:
            if self.date_of_transport:
                vals['date_done'] = self.date_of_transport

        return super(StockPickingInherit, self).write(vals)

    def _action_done(self):

        res = super(StockPickingInherit, self)._action_done()
        
        if self.date_of_transport:

            #Test if more than two months in the future
            if self.date_of_transport > fields.Date.today() + relativedelta(months=2):
                raise UserError(_("Can't post more than 2 months in to the future!\n\nPlease correct the date of transport. Or contact your system administrator."))

            #Test if less than locked date
            if self.date_of_transport < self.company_id.fiscalyear_lock_date or self.date_of_transport < self.company_id.period_lock_date:
                raise UserError(_("The selected date of transport is before the system accounting lock date.\n\nPlease correct the date of transport. Or contact your system administrator."))

            done_moves = self.mapped('move_line_ids').filtered(lambda self: self.state in ['done'])

            done_moves.with_context(bypass_reservation_update=True).write({
                'date': self.date_of_transport
            })

        return res