from odoo import api, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    @api.multi
    def update_product_reference_from_sequence(self):
        self.ensure_one()
        self.default_code = self.env["ir.sequence"].get("product.product")
