{
    'name': 'User Pricelist Restrictions',
    'version': '1.1',
    'category': 'Sales',
    'summary': 'Restrict pricelist access for certain users',
    'description': 'Allows configuration of price lists accessible only by specific users.',
    'depends': ['sale', 'product'],
    'license':'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'security/user_pricelist_restrictions_security.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
