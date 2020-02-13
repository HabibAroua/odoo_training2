# -*- coding: utf-8 -*-
from odoo import http

# class App(http.Controller):
#     @http.route('/app/app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app/app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('app.listing', {
#             'root': '/app/app',
#             'objects': http.request.env['app.app'].search([]),
#         })

#     @http.route('/app/app/objects/<model("app.app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app.object', {
#             'object': obj
#         })