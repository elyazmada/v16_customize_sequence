from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    branch_code = fields.Char(string="Branch Code", required=True)
