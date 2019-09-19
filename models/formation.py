from odoo import fields,models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class Formation(models.Model):

	_name ="formation.formation"
	_description = "formation table"

	name=fields.Char()
	prix=fields.Float()
	categorie=fields.Char()
	session_id=fields.One2many('formation.session','formation_id',string ="session")

class Atestation(models.Model):

	_name ="formation.atestation"
	_description = "atestation table"

	condidat=fields.Many2one('formation.condidat',string ="condidat")
	description=fields.Char()
	date=fields.Date()
	formation=fields.Many2one('formation.formation',string ="formation")


class Formateur(models.Model):

	_name ="formation.formateur"
	_description = "formateur table" 

	name=fields.Char()
	matricule=fields.Integer()
	diplome=fields.Char()
	sessionfo_id=fields.Many2many('formation.session','formateur_id',string ="session")
	_sql_constraints = [('unique_id','UNIQUE(matricule)',"Ce matricule  existe deja !!!"),]

class Condidat(models.Model):

	_name ="formation.condidat"
	_description = "condidat table"

	name=fields.Char()
	num_ins=fields.Integer()
	sessionCo_id=fields.Many2many('formation.session','condidat_id',string ="session")

	_sql_constraints = [('unique_id','UNIQUE(num_ins)',"Le num d'inscription existe deja !!!"),]
	
	
class Salle(models.Model):

	_name ="formation.salle"
	_description = "salle table"

	
	name=fields.Char()
	libre=fields.Boolean()
	nb_place=fields.Integer(string='capacite',default=20,required=True)
	sessionS_id=fields.Many2many('formation.session','salle_id',string ="session")

			
	
class Session(models.Model):

	_name ="formation.session"
	_description = "session table"

	@api.one
	def open(self):
		if self.state=="a":
			self.state="b"
		else:
			self.state="a"


	@api.one
	@api.constrains('date_debut','date_fin')
	def _check_date(self):

		if datetime.strptime(self.date_debut,"%Y-%m-%d") > datetime.strptime(self.date_fin,"%Y-%m-%d"):
			raise ValidationError("erreur Date")

	@api.one
	@api.depends('date_debut','date_fin')
	def compute_dure(self):

		if self.date_debut and self.date_fin:
			date_debut=datetime.strptime(self.date_debut,"%Y-%m-%d")
			date_fin=datetime.strptime(self.date_fin,"%Y-%m-%d")
			self.duree=date_fin-date_debut
		else:
			self.duree=False
	
	@api.onchange('formation_id')
	def onchange_C(self):
		self.categorie = self.formation_id.categorie
	
	name=fields.Char()
	nb_participant=fields.Integer()
	date_debut=fields.Date()
	date_fin=fields.Date()
	duree=fields.Char(string="Duree",compute="compute_dure")
	state=fields.Selection([('a', 'Disponible'), ('b', 'Occupee')],'Session')
	formation_id=fields.Many2one('formation.formation',string ="formation")
	categorie=fields.Char(string="categorie")
	formateur_id=fields.Many2many('formation.formateur',string ="formateur")
	condidat_id=fields.Many2many('formation.condidat',string ="condidat")
	salle_id=fields.Many2many('formation.salle',string ="salle")
	

	
		


	



