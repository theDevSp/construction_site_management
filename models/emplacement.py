from odoo import models, fields

class FleetVehicleChantierEmplacement(models.Model):
    
    _name = 'fleet.vehicle.chantier.emplacement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Équipe Chantier'
    
    name = fields.Char("Libellé",required=True)
    abrv = fields.Char("abbreviation",required=True)

    chantier_ids = fields.Many2many(
        'fleet.vehicle.chantier',
        string='Chantiers'
    )
