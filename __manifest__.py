# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Bills',
    'version': '0.1',
    'summary': 'Sample case double for Customer Bills',
    'description': """ Second test Customer Bills
    """,
    'depends': ['base'],
    'data': [
        # 'wizard/discount.xml',
        'wizard/gst.xml',
        'security/ir.model.access.csv',
        'views/customer.xml',
        'views/product.xml',
        ],
    'installable': True,
    'auto_install': False
}
