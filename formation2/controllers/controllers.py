# -*- coding: utf-8 -*-
from odoo import http

# class Formation2(http.Controller):
#     @http.route('/formation2/formation2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formation2/formation2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formation2.listing', {
#             'root': '/formation2/formation2',
#             'objects': http.request.env['formation2.formation2'].search([]),
#         })

#     @http.route('/formation2/formation2/objects/<model("formation2.formation2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formation2.object', {
#             'object': obj
#         })