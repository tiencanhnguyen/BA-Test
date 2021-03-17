# -*- coding: utf-8 -*-
{
    'name': "scan_qr",
    'summary': """
        Search the Sale Order.
    """,
    'description': """
        Scan the QR Code and search based on the code for the Sale Order.
    """,
    'category': 'Sales',
    'version': '0.1',
    'sequence': 6,
    'depends': ['sale_management'],
    'data': [
        'views/asset.xml',
    ],
    'qweb': [
        'static/src/xml/scan_qr_code.xml',
    ],
}
