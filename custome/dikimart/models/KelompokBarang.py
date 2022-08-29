from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'dikimart.kelompokbarang'
    _description = 'New Description'

    name = fields.Char(string='Nama Kelompok')
    kode_kelompok = fields.Char(string='Kode Kelompok')
    kode_rak = fields.Char(string='Kode Rak')
    
    
