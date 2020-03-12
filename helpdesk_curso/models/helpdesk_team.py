from odoo import api, fields, models, _

class HelpdeskTeam(models.Model):

    _name = 'helpdesk.team'

    name = fields.Char(string='Name', required=True)

    user_qty = fields.Integer(string="User quantity", compute='_compute_user_qty', store=True)

    ticket_ids = fields.One2many(comodel_name='helpdesk.ticket', inverse_name='team_id', string='Tickets')

    @api.depends('user_ids')
    def _compute_user_qty(self):
        for record in self:
            record.user_qty = len(record.user_ids)

    user_ids = fields.Many2many(
        comodel_name="res.users",
        relation="helpdesk_team_users_rel",
        column1="team_id",
        column2="user_id",
        string="Users")




