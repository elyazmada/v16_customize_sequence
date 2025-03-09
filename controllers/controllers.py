# -*- coding: utf-8 -*-
# from odoo import http


# class V16CustomizeSequence(http.Controller):
#     @http.route('/v16_customize_sequence/v16_customize_sequence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/v16_customize_sequence/v16_customize_sequence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('v16_customize_sequence.listing', {
#             'root': '/v16_customize_sequence/v16_customize_sequence',
#             'objects': http.request.env['v16_customize_sequence.v16_customize_sequence'].search([]),
#         })

#     @http.route('/v16_customize_sequence/v16_customize_sequence/objects/<model("v16_customize_sequence.v16_customize_sequence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('v16_customize_sequence.object', {
#             'object': obj
#         })
