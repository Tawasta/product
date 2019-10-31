# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProductTemplate(models.Model):

    # 1. Private attributes
    _inherit = 'product.template'
    _description = "Product template"

    detailed_description = fields.Html(
        string='More detailed description for the customer'
    )