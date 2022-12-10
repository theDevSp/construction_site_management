# -*- coding: utf-8 -*-
# from odoo import http


# class ConstructionSiteManagement(http.Controller):
#     @http.route('/construction_site_management/construction_site_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/construction_site_management/construction_site_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('construction_site_management.listing', {
#             'root': '/construction_site_management/construction_site_management',
#             'objects': http.request.env['construction_site_management.construction_site_management'].search([]),
#         })

#     @http.route('/construction_site_management/construction_site_management/objects/<model("construction_site_management.construction_site_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('construction_site_management.object', {
#             'object': obj
#         })
