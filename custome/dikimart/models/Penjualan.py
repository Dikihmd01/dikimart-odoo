from odoo.exceptions import ValidationError, UserError
from odoo import api, fields, models


class Penjualan(models.Model):
    _name = 'dikimart.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='dikimart.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['dikimart.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result

    '''
    Pemabaalan transaksi dapat menggunakan dua metode
    1. ondelete
    2. unlink
    Jika pembatalan transaksi mengguakan ondelete gagal,
    bisa menggunakan metode unlink
    '''
    @api.ondelete(at_uninstall=False)
    def __ondelete_penjualan(self):
        if self.detailpenjualan_ids:
            penjualan = []
            for line in self:
                penjualan = self.env['dikimart.detailpenjualan'].search(
                    [('penjualan_id', '=', line.id)])
                print(penjualan)

            for ob in penjualan:
                print(ob.barang_id.name + ' ' + str(ob.qty))
                ob.barang_id.stok += ob.qty

    # def unlink(self):
    #     if self.detailpenjualan_ids:
    #         penjualan = []
    #         for line in self:
    #             penjualan = self.env['dikimart.detailpenjualan'].search(
    #                 [('penjualan_id', '=', line.id)])
    #             print(penjualan)

    #         for ob in penjualan:
    #             print(ob.barang_id.name + ' ' + str(ob.qty))
    #             ob.barang_id.stok += ob.qty

    #     line = super(Penjualan, self).unlink()

    '''
    SQL constraints, strukturnya:
    (<nama constraint>, <constraintnya seperti apa>, <pesan constrain>)
    '''
    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama!')
    ]


class DetailPenjualan(models.Model):
    _name = 'dikimart.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='dikimart.penjualan',
        string='Detail Penjualan')
    barang_id = fields.Many2one(
        comodel_name='dikimart.barang',
        string='List Barang')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_barang_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_satuan

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        if self.barang_id.harga_jual:
            self.harga_satuan = self.barang_id.harga_jual

    '''
    Ketika transaksi berlangsung, barang yang sudah masuk
    ke dalam keranjang, maka stok barang akan berkurang
    sesuai dengan jumlah beli yang masuk ke kerangjang dengan
    menggunakan fungsi create().
    '''
    @api.model
    def create(self, vals):
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
            # Mendapatkan data berdasarkan ID pada barang_id
            self.env['dikimart.barang'].search(
                [('id', '=', line.barang_id.id)]
            ).write({'stok': line.barang_id.stok - line.qty})

        return line
    
    @api.constrains('qty')
    def check_quantity(self):
        for line in self:
            if line.qty < 1:
                raise ValidationError('Mau belanja barang {} ini berapa sih...'.format(line.barang_id.name))
            elif line.barang_id.stok < line.qty:
                raise ValidationError('Stok {} tidak mencukup hanya tersedia {}'.format(line.barang_id.name, line.barang_id.stok))

