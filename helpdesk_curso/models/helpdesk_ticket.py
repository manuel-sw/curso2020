from odoo import api, fields, models, _

class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')

    team_id = fields.Many2one(comodel_name='helpdesk.team', string='Team')
    stage_id = fields.Many2one(comodel_name='helpdesk.ticket.stage', string='Stage')

    user_ids = fields.Many2many(
        comodel_name="res.users",
        relation="helpdesk_ticket_users_rel",
        column1="ticket_id",
        column2="user_id",
        string="Users")

    responsable_id = fields.Many2one(comodel_name='res.users', string='Responsable')

    @api.onchange('team_id')
    def onchange_method(self):
        self.user_ids = self.team_id.user_ids

    def set_responsable(self):
        self.ensure_one()
        self.responsable_id = self.env.user
        # Haría lo mismo pero con un solo acceso a bbdd si hubiese más de un campo a cambiar
        #self.write({'responsable_id': self.env.user})
