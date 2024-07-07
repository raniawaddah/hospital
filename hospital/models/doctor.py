from odoo import fields, models, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    # _rec_name = 'id_person'
    name = fields.Char(related='doctor_id.name', store=True)

    doctor_id = fields.Many2one('hospital.person', string='Doctor',
                                required=True, domain=[('person_position', '=', 'doctor')],)

    patient_id = fields.Many2one('hospital.person', string='Patient',
                                 required=True, domain=[('person_position', '=', 'patient')],)
    date_of_reservation = fields.Datetime(string='Date Of Reservation')
    notes = fields.Html(string='Other Information')
    check = fields.Selection([
        ('children', 'Children'),
        ('dental', 'Dental'),
        ('ent', 'Ent')
    ], default='dental', required=True, string='Check')

