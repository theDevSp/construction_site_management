# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class User(models.Model):
    _inherit = ['res.users']

    chantier_responsable_ids = fields.Many2many('fleet.vehicle.chantier', 'chantier_responsable_relation', 'user_id', 'chantier_id', string="Chantier")