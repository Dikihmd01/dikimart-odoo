# from odoo import api, fields, models
from odoo import fields, models


class Konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'Contact'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
