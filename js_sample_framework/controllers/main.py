from odoo import http
from odoo.http import request

class Doc(http.Controller):

    @http.route('/page')
    def funct(self,**kw):
        return "<h1>Hello world</h1>"

    @http.route('/habib')
    def funct(self, **kw):
        return "Holal Amigos"