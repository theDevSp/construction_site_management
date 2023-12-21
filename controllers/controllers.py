# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from datetime import datetime


class ConstructionSiteManagement(http.Controller):
    @http.route('/hr_management/pointage/get_all_chantiers', type='json', auth='user')
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

    @http.route('/hr_management/users/get_all_chantiers', type='json', auth='user')
    def get_all_chantiers_for_users(self):
        try:
            chantier_records = http.request.env['fleet.vehicle.chantier'].search([
                ('type_chantier', '!=', 'CG'),
                ('id', 'in', http.request.env.user.chantier_responsable_ids.ids)
            ])

            if chantier_records:
                data = []
                for record in chantier_records:
                    data.append({
                        'id': record.id,
                        'name': record.simplified_name
                    })

                response_data = {
                    'code': 200,
                    'message': 'Les données ont été chargées avec succès.',
                    'timestamp': datetime.now().isoformat(),
                    'data': data
                }
                return response_data

            else:
                response_data = {
                    'code': 202,
                    'message': "Aucune Chantier à charger",
                    'timestamp': datetime.now().isoformat()
                }
                return response_data

        except Exception as e:
            error_message = {
                'code': 504,
                'error': f'An error occurred while processing the request. {e}',
                'message': "Une erreur s'est produite, veuillez réessayer !",
                'timestamp': datetime.now().isoformat()
            }
            return error_message
