from odoo import fields, models, api, _
# from odoo.exceptions import ValidationError


class HospitalReservation(models.Model):
    _name = 'hospital.reservation'
    # _rec_name = 'id_person

    doctor_name = fields.Many2one('hospital.person', domain=[('person_position', '=', 'doctor')],
                                  string='Doctor Name',required=True)

    patient_name = fields.Many2one('hospital.person', domain=[('person_position', '=', 'patient')],
                                   string='Patient Name', required=True)

    responsible = fields.Many2one('res.users', string='Responsible',
                                  default=lambda self: self.env.user, readonly=True, required=True)

    reservation_date = fields.Datetime(string='Reservation Date',
                                       default=lambda self: fields.Datetime.now(), required=True)

    currency_id = fields.Many2one('res.currency')
    # price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_price_subtotal')

    # amount_total =fields.Monetary(string='Total Tax Included')

    # def _compute_price_subtotal(self):
    #     for rec in self:
    #         rec.price_subtotal = rec.reservation_price



    email = fields.Char(string='Email', related='responsible.login',
                        readonly=True, store=True)

    notes = fields.Html(string='Other Information')

    check_type = fields.Selection([
        ('children', 'Children'),
        ('dental', 'Dental'),
        ('ent', 'Ent')
    ], default='dental', required=True, string='Check Type')

    # name = fields.Char(related='doctor_id.name', store=True)

    reservation_price = fields.Float(string='Reservation Price')
    reservation_number = fields.Float(string='Reservation Number')
    total = fields.Float('Total', compute='get_total_amount', readonly=True)

    @api.depends('reservation_price', 'reservation_number')
    def get_total_amount(self):
        for rec in self:
            rec.total = rec.reservation_price * rec.reservation_number

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirmed'),
        ('send_to_doctor','Sent To Doctor'),
        ('send_to_patient','Sent To Patient'),
        ('done','Done'),
        ('cancel','Cancelled'),
    ], default='draft', string='States')

    def send_to_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def send_to_doctor(self):
        for rec in self:
            rec.state = 'send_to_doctor'

    def send_to_done(self):
        for rec in self:
            rec.state = 'done'

    def send_to_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def send_to_draft(self):
        for rec in self:
            rec.state = 'draft'

    def send_to_patient(self):
        for rec in self:
            rec.state = 'send_to_patient'
