# -*- coding: utf-8 -*-
from odoo import models, fields, api

class empleado(models.Model):
    _name = 'indomin.empleado'
    _description = 'indomin.empleado'

    photo = fields.Binary(string = "FOTOGRAFÍA")
    dni = fields.Char(string = "DNI", required = True)
    name = fields.Char(string = "NOMBRE Y APELLIDO", required = True)
    exp = fields.Text(string = "EXPERIENCIA LABORAL")
    fecha_nac = fields.Date(string = "FECHA DE NACIMIENTO", required = True)
    hab = fields.Boolean(string = "DISPONIBILIDAD")