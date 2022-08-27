# -*- coding: utf-8 -*-
# from odoo import http


# class Dikimart(http.Controller):
#     @http.route('/dikimart/dikimart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dikimart/dikimart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dikimart.listing', {
#             'root': '/dikimart/dikimart',
#             'objects': http.request.env['dikimart.dikimart'].search([]),
#         })

#     @http.route('/dikimart/dikimart/objects/<model("dikimart.dikimart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dikimart.object', {
#             'object': obj
#         })
