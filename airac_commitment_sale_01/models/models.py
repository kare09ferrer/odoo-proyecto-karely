# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'

    commitment_date = fields.Datetime(string='Fecha de Entrega Compromiso', required=False, default='', help='Este campo es para definir la fecha de entrega Compromiso de la Orden de Trabajo en Manufactura para el pedido en cuestion.')
