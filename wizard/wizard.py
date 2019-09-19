from odoo import fields,models,api,_
from datetime import datetime


class wizard(models.TransientModel):
	_name='formation.wizard'

	
	@api.multi
	def confirmer(self):
		session_id=self.env.context.get('active_id')
		session=self.env['formation.session'].browse(session_id)
		for condidat in session.condidat_id:
			self.env["formation.atestation"].create({
				'date':self.date,
				'description':self.description,
				'condidat':condidat.id,
				'formation':session.formation_id.id,

				})

	@api.multi
	def afficher(self):
		session_id=self.env.context.get('active_id')
		session=self.env['formation.session'].browse(session_id)
		return session.condidat_id


	date =fields.Date()
	description=fields.Char()
	condidat_id=fields.Many2many('formation.condidat','atestation_candidat','atestation_id','condidat_id',default=afficher,string ="condidat")


	