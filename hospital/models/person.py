from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class HospitalPerson(models.Model):
    _name = 'hospital.person'
    # _rec_name = 'id_person'

    name = fields.Char(string='Name', required=True)
    id_person = fields.Char(string='ID', required=True)
    user_ids = fields.Many2many('res.users', string='Responsible')
    phone = fields.Char(string='Phone', required=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    photo = fields.Binary(string='Image')
    married = fields.Boolean(string='Married?')
    notes = fields.Html(string='Other Information')
    children_number = fields.Integer(string='Children Number')
    gender_type = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True, string='Gender Type')
    person_position = fields.Selection([
        ('doctor', 'Doctor'),
        ('patient', 'Patient')
    ], required=True, string='Person Position')

    # doctor_reservation_ids = fields.One2many('hospital.doctor', 'doctor_id', string='Doctor Reservations')

    patient_reservation_ids = fields.One2many('hospital.reservation', 'patient_name', string='Patient Reservations')
    doctor_reservation_ids = fields.One2many('hospital.reservation', 'doctor_name', string='Doctor Reservations')

    def print_some_thing(self):
        hello = 'Hello Odoo15'
        print(hello)


    @api.constrains('phone', 'children_number')
    def _ckeck_phone_validation_constraint(self):
        for rec in self:
            if rec.children_number < 0:
                raise ValidationError('Children number must be >= 0   !!!!!')
            if rec.phone[0] !='0' and rec.phone[1] !='1':
                raise ValidationError('Phone Number Is Not Valid (Must Start with (01) !!!!!')
            if len(rec.phone) !=11 :
                raise ValidationError('Phone Number Is Not Valid (Not 11 Digit )!!!!!')
            for number in rec.phone:
                if number not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    raise ValidationError('Phone Number Is Not Valid (All Number must be digits only )!!!!!')

            phone_numbers = self.search([('id', '!=', rec.id), ('phone', '=', rec.phone)])
            if phone_numbers:
                raise ValidationError('Phone Number must be unique !!!!!')

