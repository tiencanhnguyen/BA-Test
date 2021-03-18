# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[('ahamove_vietnam', "Ahamove Vietnam")])
    currency_id = fields.Many2one(comodel_name='res.currency', default=lambda self: self.env.company.currency_id)
    min_shipping_fee = fields.Monetary(string='Min shipping  fee', currency_field='currency_id')
    tax = fields.Selection([('tax_include', 'TAX Included'), ('tax_exclude', 'TAX Excluded')],
                           string='Tax')
    max_quantities_per_order = fields.Integer(string='Max quantities per order (per Sales order)')
    min_quantities_per_order = fields.Integer(string='Min quantities per order (per Sales order)')
    max_amount_per_order = fields.Monetary(string='Max amount per order', currency_field='currency_id')
    min_amount_per_order = fields.Monetary(string='Min amount per order', currency_field='currency_id')
    payment_type = fields.Many2one(comodel_name='payment.type', string='Payment type')
    site_id = fields.Char(string='SiteID')
    password = fields.Char(string='Password')
    account_number = fields.Char(string='Account Number')
    api_key = fields.Char(string='API Key')
    pricing_type = fields.Selection([('fixed_price', 'Fixed Price'), ('based_on_rules', 'Based on Rules')])
    description = fields.Html(string='Description')

    def _compute_can_generate_return(self):
        super(DeliveryCarrier, self)._compute_can_generate_return()
        for carrier in self:
            if carrier.delivery_type == 'ahamove_vietnam':
                carrier.can_generate_return = True

    def _get_price_from_picking(self, total, weight, volume, quantity):
        price = 0.0
        criteria_found = False
        price_dict = {'price': total, 'volume': volume, 'weight': weight, 'wv': volume * weight, 'quantity': quantity,
                      'distance_km': weight, 'distance_m': weight}
        if self.free_over and total >= self.amount:
            return 0
        for line in self.price_rule_ids:
            test = safe_eval(line.variable + line.operator + str(line.max_value), price_dict)
            if test:
                price = line.list_base_price + line.list_price * price_dict[line.variable_factor]
                criteria_found = True
                break
        if not criteria_found:
            raise UserError(_("No price rule matching this order; delivery cost cannot be computed."))

        return price

    def ahamove_vietnam_rate_shipment(self, order):
        return self.base_on_rule_rate_shipment(order)
