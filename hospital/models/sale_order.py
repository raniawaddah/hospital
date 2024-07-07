from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    cost2= fields.Float(string='Cost 2')
    cost2= fields.Float(string='Cost 2')
    def action_submit (self):
        print("Hello")

# class SaleOrderLine(models.Model):
#     _inherit ='sale.order.line'
#     note = fields.Char(string='Notes')



    sale_order_type = fields.Selection([
        ('special', 'Special'),
        ('general', 'General'),
    ],
        string='Sale Order Type',)

    id_person = fields.Many2one('hospital.person', string='Id Person')
    # phone = fields.Char( string='Phone', related='id_person.phone', readonly='True')
    phone = fields.Char( string='Phone', compute='_get_person_phone', readonly='True')


    def _get_person_phone(self):
        for rec in self:
            rec.phone = rec.id_person.phone