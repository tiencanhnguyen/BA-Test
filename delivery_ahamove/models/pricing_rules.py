# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PricingRules(models.Model):
    _inherit = 'delivery.price.rule'

    delivery_type = fields.Selection(related='carrier_id.delivery_type')

    variable = fields.Selection(selection_add=[('distance_km', 'Distance (km)'), ('distance_m', 'Distance (m)')])
    rounding = fields.Selection([('up', 'UP'), ('down', 'Down'), ('4/5', '4/5')], string='Rounding')
    variable_factor = fields.Selection(selection_add=[('distance_km', 'Distance (km)'), ('distance_m', 'Distance (m)')])
    from_date = fields.Datetime(string='From date')
    to_date = fields.Datetime(string='To date')
    exclude_date_id = fields.One2many(comodel_name='exclude.date', inverse_name='price_rule_id', string='Exclude dates')


class ExcludeDate(models.Model):
    _name = 'exclude.date'

    price_rule_id = fields.Many2one(comodel_name='delivery.price.rule')
    exclude_date = fields.Date(string='Add Exclude dates')
