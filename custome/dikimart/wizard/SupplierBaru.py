from odoo import api, fields, models


class SupplierBaru(models.TransientModel):
    _name = 'dikimart.supplierbaru'

    supplier_id = fields.Many2one(comodel_name='dikimart.supplier', string='Nama Supplier')
    barang_id = fields.Many2many(
        comodel_name='dikimart.barang',
        string='Barang')
    
    def button_supplier_baru(self):
        pass
    
    
