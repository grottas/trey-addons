# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    sold_id = fields.Many2one(
        comodel_name='product.sold',
        string='Product Sold')
