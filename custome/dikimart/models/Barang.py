from odoo import api, fields, models


class Barang(models.Model):
    _name = 'dikimart.barang'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    
    
    
