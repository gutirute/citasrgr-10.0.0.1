# -*- coding: utf-8 -*-

from odoo import models, fields, api

class citasrgr(models.Model):
    _name = 'citasrgr.citasrgr'

    autor = fields.Many2one('res.users', default = lambda self: self.env.user)
    fecha_visualizacion = fields.Date(default=fields.Date.today)
    orden = fields.Integer()
    cita = fields.Text(required=True)

    @api.onchange('fecha_visualizacion')
    def _onchange_fecha(self):
	cr=self.env.cr
	valor=str(self.fecha_visualizacion)
	try:
        	cr.execute("SELECT count(*) FROM citasrgr_citasrgr AS a WHERE (CAST(a.fecha_visualizacion AS varchar(20)) LIKE '%s')" % (valor))
		cont=cr.fetchone()[0]
	except:
		cont=0
	self.orden = cont+1;
