from odoo import http
from odoo.http import request

class Doc(http.Controller):

    @http.route('/page')
    def funct(self,**kw):
        return "<h1>Hello world</h1>"

    @http.route('/habib' , type="http")
    def funct(self, **kw):
        return "Holal Amigos"

    @http.route('/test/path', type='http', methods=['POST'],csrf=False)
    def test_path(self, **kw):
        # here in kw you can get the inputted value
        x1=int(kw['a1'])
        x2=int(kw['a2'])
        x= x1+x2
        print ('the sum is ',x)
        return 'The sum is '+str(x)


    @http.route('/custom/url' , website=True , auth='public')
    def show_custom_webpage(self, **kw):
        return request.render('js_sample_framework.new_web_page', {})