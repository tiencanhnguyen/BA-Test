# -*- coding: utf-8 -*-

{
    'name': 'Delivery Ahamove',
    'category': 'Operations/Inventory/Delivery',
    'summary': 'Send your shippings through Ahamove',
    'description': """
    ID 2457378
    Compute shipping costs and ship with Ahamove""",
    "author": "odooPS",
    "website": "https://www.odoo.com",
    'depends': [
        'sale_management',
        'delivery',
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_carrier_views.xml',
        'views/pricing_rule_views.xml',
        'views/payment_type_views.xml',
        'views/res_config_settings_views.xml'
    ],
    'application': True,
}
