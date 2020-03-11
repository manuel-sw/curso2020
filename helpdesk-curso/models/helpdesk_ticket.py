from odoo import api, fields, models, _

class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')