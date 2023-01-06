from odoo import models, fields

class FleetVehicleChantierEmplacement(models.Model):
    
    _name = 'fleet.vehicle.chantier.emplacement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Chantier'
    
    name = fields.Char("Libellé",required=True)

    chantier_ids = fields.Many2many(
        'fleet.vehicle.chantier',
        string='Chantiers'
    )
