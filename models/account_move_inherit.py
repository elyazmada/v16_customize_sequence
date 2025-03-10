from odoo import models, fields, api
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_journal_code(self):
        return self.journal_id.code if self.journal_id else 'JRN'
    
    @api.model
    def create(self, vals):
        branch_code = self.env.user.company_id.branch_code or 'NA'  
        record = super(AccountMove, self).create(vals)
        journal_code = record._get_journal_code()
        invoice_date = record.invoice_date or fields.Date.today()
        year = invoice_date.strftime('%y')
        month = invoice_date.strftime('%m')

        if record.move_type == 'out_invoice':  # Invoice
            sequence = self.env['ir.sequence'].next_by_code('account.move.invoice') or '/'
            record.name = f'INV/{branch_code}/{year}/{month}/{sequence}'
        elif record.move_type == 'in_invoice':  # Bills
            sequence = self.env['ir.sequence'].next_by_code('account.move.bill') or '/'
            record.name = f'BILLS/{branch_code}/{year}/{month}/{sequence}'
        elif record.move_type == 'entry':  # Journal Entries
            sequence = self.env['ir.sequence'].next_by_code('account.move.journal') or '/'
            record.name = f'{journal_code}/{branch_code}/{year}/{month}/{sequence}'

        return record
