# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pricingRules(models.Model):
    _inherit = 'delivery.price.rule'

    delivery_type = fields.Selection(related='carrier_id.delivery_type')

    variable = fields.Selection(selection_add=[('distance_km', 'Distance (km)'), ('distance_m', 'Distance (m)')])
    rounding = fields.Selection([('up', 'UP'), ('down', 'Down'), ('4/5', '4/5')], string='Rounding')
    variable_factor = fields.Selection(selection_add=[('distance_km', 'Distance (km)'), ('distance_m', 'Distance (m)')])
    from_date = fields.Datetime(string='From date')
    to_date = fields.Datetime(string='To date')
    exclude_date = fields.Date(string='Exclude date')
