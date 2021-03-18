# -*- coding: utf-8 -*-

from odoo import models, fields


class PaymentType(models.Model):
    _name = 'payment.type'
    _rec_name = 'payment_type'

    payment_type = fields.Char(string='Payment Type')
