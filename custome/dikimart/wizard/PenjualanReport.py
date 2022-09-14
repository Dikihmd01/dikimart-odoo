from odoo import api, fields, models


class SupplierBaru(models.TransientModel):
    _name = 'dikimart.penjualanreport'
    

    konsumen_id = fields.Many2one(
        comodel_name='res.partner',
        string='Konsumen')
    dari_tanggal = fields.Date(string='Dari Tanggal')
    ke_tanggal = fields.Date(string='Ke Tanggal')
    
    def action_penjualan_report(self):
        filter = []
        konsumen_id = self.konsumen_id
        dari_tgl = self.dari_tanggal
        ke_tgl = self.ke_tanggal

        if konsumen_id:
            filter += [('nama_pembeli', '=', konsumen_id.id)]
        if dari_tgl:
            filter += [('tgl_penjualan', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        print(filter)
        penjualan = self.env['dikimart.penjualan'].search_read(filter)
        print(penjualan)
        data = {
            'form': self.read()[0],
            'penjualanxx': penjualan,
        }
        print(data)
        return self.env.ref('dikimart.wizzard_penjualanreport_pdf').report_action(self, data=data)