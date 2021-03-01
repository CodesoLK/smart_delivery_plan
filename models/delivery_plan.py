from flectra import fields, api, models, _
from datetime import date,datetime,timedelta
from flectra.addons import decimal_precision as dp

class PendingDeliveryPlan(models.Model):

    _inherit = 'sale.order.line'

    qty_delivery_available = fields.Float(
        compute='_get_available_qty', string='To Deliver', store=True, readonly=True,
        digits=dp.get_precision('Product Unit of Measure'))
    order_date = fields.Date(compute='_get_order_date', store=True, readonly=True)

    @api.depends('qty_delivered')
    def _get_available_qty(self):
        """
        Compute the quantity to be delivered. .
        """
        for line in self:
            if line.product_uom_qty and line.qty_delivered:
                line.qty_delivery_available = line.product_uom_qty - line.qty_delivered

    @api.depends('order_id')
    def _get_order_date(self):
        """Compute the order date"""
        for line in self:
            if line.order_id.confirmation_date:
                line.order_date = line.order_id.confirmation_date