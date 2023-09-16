# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ConstructionSiteManagement(http.Controller):
    @http.route('/construction_site_management/fetch_list/', type='json', auth='user')
    def get_chantier_list(self):
        chantier_object = http.request.env['fleet.vehicle.chantier']
        res = []
        domain = []
        all_group = http.request.env['res.users'].has_group("construction_site_management.group_access_all")
        dig_group = http.request.env['res.users'].has_group("construction_site_management.group_access_digital")
        aff_group = http.request.env['res.users'].has_group("construction_site_management.group_access_affectation")

        if dig_group:
            domain = [('digital','=',True),('type_chantier','!=','CG')]
            for line in chantier_object.search(domain):
                res.append({
                    'id':line.id,
                    'name':line.name,
                    'code':line.code if line.code else '####'
                })
        elif aff_group:
            for line in http.request.user.chantier_responsable_ids:
                res.append({
                    'id':line.id,
                    'name':line.name,
                    'code':line.code if line.code else '####'
                })
        elif all_group:
            domain.clear()
            for line in chantier_object.search(domain):
                res.append({
                    'id':line.id,
                    'name':line.name,
                    'code':line.code if line.code else '####'
                })

        return {
            'result':res
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
