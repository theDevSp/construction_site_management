# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class construction_site_management(models.Model):
#     _name = 'construction_site_management.construction_site_management'
#     _description = 'construction_site_management.construction_site_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
