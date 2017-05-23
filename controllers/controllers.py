# -*- coding: utf-8 -*-
from odoo import http

# class Citasrgr(http.Controller):
#     @http.route('/citasrgr/citasrgr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasrgr/citasrgr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasrgr.listing', {
#             'root': '/citasrgr/citasrgr',
#             'objects': http.request.env['citasrgr.citasrgr'].search([]),
#         })

#     @http.route('/citasrgr/citasrgr/objects/<model("citasrgr.citasrgr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasrgr.object', {
#             'object': obj
#         })