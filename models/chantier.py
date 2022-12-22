from odoo import models, fields, api
from odoo.exceptions import UserError

class fleet_vehicle_chantier(models.Model):
	_name = 'fleet.vehicle.chantier'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Chantier'

	name = fields.Char('Nom Chantier', required=True)
	code = fields.Char('Code Chantier', readonly=True, required=True, copy=False, default='New')
	ville = fields.Char('Ville')
	active = fields.Boolean('Actif', help="Cacher le chantier sans le supprimer.", default=True)
	digital = fields.Boolean('Informatisé', help="Chantier informatisé", default=True)

	location_id = fields.Many2one('stock.location', 'Location', readonly=True)
	
	chantier_parent_id = fields.Many2one('fleet.vehicle.chantier','Chantier Parent')
	chantier_ids = fields.One2many('fleet.vehicle.chantier','chantier_parent_id','Chantiers Liés',readonly=True)
	
    #zone_id = fields.Many2one('fleet.zone.zone', 'Zone')

	type_chantier = fields.Selection(
		[('Chantier', 'Chantier Principale'), ('Atelier/Stock', 'Atelier/Stock'), ('Citerne Gasoil', 'Citerne Gasoil'),
		 ('Poste Enrobé', 'Poste Enrobé')],
		string="Type Chantier", required=True)

	emplacement_ids = fields.Many2many(
		'fleet.vehicle.chantier.emplacement',
		string='Emplacements'
    )

	responsables_ids= fields.Many2many(
        'responsable.chantier',
        string = 'Responsables :',
    )

	_sql_constraints = [
		('code_uniq', 'UNIQUE(code)', 'Ce code de chantier est déjà utilisé.'),
	]

	@api.model
	def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
		args = args or []
		domain = []
		if name:
			domain = ['|', ('name', operator, name), ('code', operator, name)]
		return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

	@api.model
	def create(self, vals):
		data_location_chantier = {
			"name": vals.get("name"),
			'usage': 'internal',
		}
		location_id = self.env['stock.location'].create(data_location_chantier)

		vals['location_id'] = location_id.id
		vals['code'] = self.env['ir.sequence'].next_by_code('fleet.vehicle.chantier.sequence') or '/'
		if vals['type_chantier'] == 'Citerne Gasoil':
			vals['name'] = vals['name'].title()
			vals['digital'] = False
		else:
			vals['name'] = vals['name'].upper()
		return super(fleet_vehicle_chantier, self).create(vals)

	
	def write(self, vals):
		if vals.get('location_id'):
			vals.pop('location_id')
		return super().write(vals)

	def action_create_citerne(self):
		if self.type_chantier != 'Chantier':
			raise UserError('Vous pouvez associer une Citerne Gasoil que pour un chantier ou ouvrage')

		data_citerne_chantier = {
			'name': self.name.title()+' (Citerne Gasoil)',
			'type_chantier': 'Citerne Gasoil',
			'ville': self.ville,
			#'zone_id': self.zone_id.id,
			'digital': False,
			'chantier_parent_id': self.id
		}
		self.env['fleet.vehicle.chantier'].create(data_citerne_chantier)