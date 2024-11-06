from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_pricelists = fields.Many2many(
        'product.pricelist',
        'user_pricelist_rel',
        'user_id',
        'pricelist_id',
        string="Allowed Pricelists"
    )
