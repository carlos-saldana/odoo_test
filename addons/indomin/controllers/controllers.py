# -*- coding: utf-8 -*-
# from odoo import http


# class Indomin(http.Controller):
#     @http.route('/indomin/indomin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/indomin/indomin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('indomin.listing', {
#             'root': '/indomin/indomin',
#             'objects': http.request.env['indomin.indomin'].search([]),
#         })

#     @http.route('/indomin/indomin/objects/<model("indomin.indomin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('indomin.object', {
#             'object': obj
#         })
