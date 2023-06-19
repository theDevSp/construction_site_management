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
	
	simplified_name = fields.Char('Nom Simplifié')
	cofabri = fields.Boolean('Cofabri')
	grant_modification = fields.Boolean('Autoriser modification')
	periodicite = fields.Selection([("1","Quinzaine"),("2","Mensuelle")],default="1",string="Périodicité",tracking=True)
	heure_normal = fields.Float('Plafond Heures de travails')
	historique_heure_normal_chantier = fields.One2many('historique.heur.normal.chantier','chantier_id', string="Historique heure normale")

    #zone_id = fields.Many2one('fleet.zone.zone', 'Zone')

	type_chantier = fields.Selection(
		[('Chantier', 'Chantier Principale'),('Depot','Dépôt / Dépôt(ANX)'), ('Atelier/Stock', 'Atelier/Stock'), ('CG', 'Citerne Gasoil'),
		 ('Poste', 'Poste Enrobé')],
		string="Type Chantier", required=True)

	emplacement_ids = fields.Many2many(
		'fleet.vehicle.chantier.emplacement',
		string='Équipes'
    )

	responsables_ids= fields.Many2many(
        'hr.responsable.chantier','id',
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
	
	def name_get(self):
		result = []
		for chantier in self:
			name = chantier.code + ' - ' + chantier.name
			result.append((chantier.id, name))
		return result

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


	# def name_get(self):
	# 	res = super(fleet_vehicle_chantier, self).name_get()
	# 	data = []
	# 	for country in self:
	# 		display_value = ''
	# 		display_value += country.code or ""
	# 		display_value += ' - '
	# 		display_value += country.name or ""
	# 		data.append((country.id, display_value))
	# 		return data



class historique_heure_normal_chantier(models.Model):

    _name = "historique.heur.normal.chantier"

    heure_normal = fields.Float('Plafond Heures de travail')
    day = fields.Date('Date d\'application') 
    chantier_id = fields.Many2one("fleet.vehicle.chantier",u"Chantier")