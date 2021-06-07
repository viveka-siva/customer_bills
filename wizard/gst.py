from odoo import models, fields


class CustomerGst(models.TransientModel):
    _name = 'customer.details'

    gst = fields.Char('GST Number:')

    def gst_number(self):
        active_id = self.env.context.get('active_id', False)
        active_ids = self.env.context.get('active_ids', False)
        active_model = self.env.context.get('active_model', False)
        gstnumber = self.env['market.product'].browse(active_ids)
        number = self.gst
        gstnumber.write({'gst_number': number})







