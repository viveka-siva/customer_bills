from odoo import models, fields, api


class Customer(models.Model):
    _name = 'market.product'
    name = fields.Char(string='Customer Name:')
    quantity = fields.Integer(string='Quantity')
    price = fields.Integer(string='Price')
    location = fields.Char('Location', size=30, required=True)
    total = fields.Integer(string='Amount')
    bill_lines_ids = fields.One2many('bill.line','product_id', string="Product Bills")
    gst_number = fields.Char(string="GST Number:")

   # def calculate_total(self):
   #  for order in orders:
   #      total = order.total
   #      discount = total * discount_percent / 100
   #      discounted_amount = total - discount
   #      order.write({'total': discounted_amount})


    def calculate_total(self):
        sum = 0
        for rec in self.bill_lines_ids:
            sum += rec.total
            self.write({'total': sum})
        return True
