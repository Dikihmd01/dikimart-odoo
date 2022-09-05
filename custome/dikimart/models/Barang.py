# from odoo import api, fields, models
from odoo import fields, models


class Barang(models.Model):
    _name = 'dikimart.barang'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    # Comodel adalah menentukkan model mana yang menjadi one-nya
    kelompokbarang_id = fields.Many2one(comodel_name='dikimart.kelompokbarang',
                                        string='Kelompok Barang',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(
        comodel_name='dikimart.supplier',
        string='Supplier')
    stok = fields.Integer(string='Stok')
    
    _sql_constraints = [
        ('stok_tidak_cukup', 'CHECK(stok >= 0)', 'Stok yang tersedia tidak mencukupi.')
    ]
