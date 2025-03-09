from odoo import models, fields, api
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals):
        branch_code = self.env.user.company_id.branch_code or 'NA'
        journal = self.env['account.journal'].browse(vals.get('journal_id'))
        journal_code = journal.code or 'JRN'
        invoice_date = fields.Date.from_string(vals.get('invoice_date')) or fields.Date.today()
        year, month = invoice_date.strftime('%y'), invoice_date.strftime('%m')

        move_type = vals.get('move_type', 'entry' if journal.type in ['general', 'bank', 'cash'] else None)
        sequence_map = {
            'out_invoice': ('account.move.invoice', f'INV/{branch_code}/{year}/{month}/'),
            'in_invoice': ('account.move.bill', f'BILLS/{branch_code}/{year}/{month}/'),
            'entry': ('account.move.journal', f'{journal_code}/{branch_code}/{year}/{month}/')
        }

        if move_type in sequence_map:
            sequence_code, prefix = sequence_map[move_type]
            sequence = self.env['ir.sequence'].next_by_code(sequence_code) or '/'
            vals['name'] = f'{prefix}{sequence}'

        return super().create(vals)
