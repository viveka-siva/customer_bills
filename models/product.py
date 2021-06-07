from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Product(models.Model):
    _name = 'bill.line'
    product_name = fields.Char(string = "Product Name:")
    quantity = fields.Integer(string='Quantity')
    unit_price = fields.Integer(string='Unit Price')
    total = fields.Integer('Total', required=True)
    product_id = fields.Many2one('market.product', string='Bill Lines')


    # def create(self,vals):
    #     qty=vals.get('quantity',0)
    #     price=vals.get('price,',0)
    #     vals.update({'total':qty*price})
    #     return super(Product, self).create(vals)
    #
    # def write(self,vals):
    #     print('self',self)
    #     #self is a recordset
    #     print('vals',vals)
    #     if vals.get('quantity',False) or vals.get('price'):
    #         print('enter if statement')
    #         qty=vals.get('quantity',False)
    #         print('quantity',0)
    #         print('quantity',qty)
    #         price=vals.get('price',0)
    #         print('price',price)
    #         if not qty:
    #             print('in if not qty')
    #             qty=self.quantity
    #         if not price:
    #             print('in if not price')
    #             #get price from record
    #             price=self.price
    #             print('quantity',qty)
    #             print('price',price)
    #             vals.udate({'total':qty*price})
    #     print(vals)
    #     return super(Product, self).write(vals)

    # def calculate_total(self):
    #     sum = 0
    #     for rec in self.product_id:
    #        sum += rec.total
    #        self.write({'total': sum})
    #     return True
