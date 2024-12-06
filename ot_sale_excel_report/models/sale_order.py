# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from datetime import datetime
from io import BytesIO
import xlsxwriter

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    excel_file = fields.Binary('Download report Excel', attachment=True, readonly=True)
    file_name = fields.Char('Excel File', size=64)

    def generate_excel(self):
        """
        This function generates an Excel report for the current Sale Order.
        The report includes the company's and customer's details, order lines, and total balance.

        Parameters:
        self (sale.order): The Sale Order record for which the Excel report is being generated.

        Returns:
        dict: A dictionary representing an action to download the generated Excel file.
        """
        filename = "Sales %s" % self.name

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        font_size_10 = workbook.add_format({
            'font_name': 'KacstBook',
            'font_size': 12,
            # 'align': 'center',
            # 'valign': 'vcenter',
            'text_wrap': True,
            'border': 1
        })
        table_header_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'bg_color': '#AAB7B8',
            'font_size': 11,
            'align': 'center',
            'valign': 'vcenter',
            'text_wrap': True
        })
        table_cell_format = workbook.add_format({
            # 'bold': 1,
            'border': 1,
            # 'bg_color': '#AAB7B8',
            'font_size': 10,
            'align': 'center',
            'valign': 'vcenter',
            'text_wrap': True
        })

        sheet = workbook.add_worksheet('data')
        sheet.set_column(0, 10, 20)
        # [sheet.set_row(idx, 20) for idx in range(10)]
        sheet.set_row(3, 60)
        sheet.set_row(4, 60)
        company = self.env.company
        sheet.insert_image('A1:B2', company.logo)
        sheet.write('A3', company.name, font_size_10)
        sheet.merge_range('A4:C5', '''%s,\n%s,\n%s - %s - %s,\n%s,''' % (company.street,
                                                                         company.street2,
                                                                         company.city,
                                                                         company.state_id.name,
                                                                         company.zip,
                                                                         company.country_id.name), font_size_10)
        sheet.merge_range('D4:F5', '''%s,\n%s,\n%s,\n%s - %s - %s,\n%s''' % (self.partner_id.name,
                                                                             self.partner_id.street,
                                                                             self.partner_id.street2,
                                                                             self.partner_id.city,
                                                                             self.partner_id.state_id.name,
                                                                             self.partner_id.zip,
                                                                             self.partner_id.country_id.name), font_size_10)

        headers = ['Product', 'Label', 'Quantity', 'Delivered', 'Invoiced', 'UoM', 'Unit Price', 'Tax', 'Disc.%',
                   'Subtotal']
        [sheet.write(5, idx, h , table_header_format)  for idx , h in enumerate(headers)]

        row = 6
        for line in self.order_line:
            sheet.write(row, 0, line.product_id.name, table_cell_format)
            sheet.write(row, 1, line.name, table_cell_format)
            sheet.write(row, 2, line.product_uom_qty, table_cell_format)
            sheet.write(row, 3, line.qty_delivered, table_cell_format)
            sheet.write(row, 4, line.qty_invoiced, table_cell_format)
            sheet.write(row, 5, line.product_uom.name, table_cell_format)
            sheet.write(row, 6, line.price_unit, table_cell_format)
            sheet.write(row, 7, ','.join([tax.name for tax in line.tax_id]), table_cell_format)
            sheet.write(row, 8, line.discount, table_cell_format)
            sheet.write(row, 9, line.price_subtotal, table_cell_format)
            row += 1

        move_line_obj = self.env['account.move.line']
        balance = move_line_obj.search([('partner_id', '=', self.partner_id.id)]).mapped('balance')
        sheet.write(row + 1, 0, 'Total Balance')
        sheet.write(row + 1, 1, sum(balance))

        workbook.close()
        output.seek(0)

        self.write({'file_name': filename + str(datetime.today().strftime('%Y-%m-%d')) + '.xlsx'})
        self.excel_file = base64.encodebytes(output.getvalue())

        # self.excel_file = base64.b64encode(output.read())

        return {
            'type': 'ir.actions.act_url',
            'name': filename,
            'url': '/web/content/sale.order/%s/excel_file?download=true' % self.id,
            'target': 'new'
        }
