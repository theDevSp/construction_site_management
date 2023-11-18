# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ConstructionSiteManagement(http.Controller):
    @http.route('/construction_site_management/get_all_chantiers', type='json', auth='user')
    def get_all_chantiers(self):

        chantier_records = http.request.env['fleet.vehicle.chantier'].search([
            ('type_chantier', '!=', 'CG')
        ])

        data = []

        for record in chantier_records:

            data.append({
                'id': record.id,
                'name': record.name,
            })

        if data:
            return data
        else:
            return {
                'code': 504,
                'msg': 'error'
            }

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
