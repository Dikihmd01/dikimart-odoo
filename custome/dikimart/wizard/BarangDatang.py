from odoo import api, fields, models


'''
Membuat model BarangDarang yang inherit
ke Transient Model, Odoo 14 ke atas harus
di daftarkan di security
'''
class BarangDatang(models.TransientModel):
    _name = 'dikimart.barangdatang'

    barang_id = fields.Many2one(comodel_name='dikimart.barang', string='Nama Barang', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_barang_datang(self):
        for line in self:
            self.env['dikimart.barang'].search([('id', '=', line.barang_id.id)]).write(
                {'stok': line.barang_id.stok +  line.jumlah}
            )

