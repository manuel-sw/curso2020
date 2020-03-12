from odoo import api, fields, models, _

class HelpdeskTicketStage(models.Model):

    _name = 'helpdesk.ticket.stage'
    _description = 'Helpdesk Ticket Stage'

    name = fields.Char()

