from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'dikimart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('makanan basah', 'Makanan Basah'),
        ('makanan kering', 'Makanan Kering'),
        ('minuman', 'Minuman'),
        ('mie instan', 'Mie Instan')
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='dikimart.barang',
                                 inverse_name='kelompokbarang_id',
                                 string='Daftar Barang')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'makanan basah':
            self.kode_kelompok = 'MAK01'
        elif self.name == 'makanan kering':
            self.kode_kelompok = 'MAK02'
        elif self.name == 'minuman':
            self.kode_kelompok = 'MIN01'
        elif self.name == 'mie instan':
            self.kode_kelompok = 'MIE01'
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['dikimart.barang'].search(
                [('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a

    daftar = fields.Char(string='Daftar isi')
    
