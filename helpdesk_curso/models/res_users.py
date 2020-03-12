from odoo import api, fields, models, _

class ResUsers(models.Model):

    _inherit = 'res.users'

    helpdesk_ticket_ids = fields.Many2many(
        comodel_name="helpdesk.ticket",
        relation="helpdesk_ticket_users_rel",
        column1="user_id",
        column2="ticket_id",
        string="Helpdesk Tickers")

    helpdesk_team_ids = fields.Many2many(
        comodel_name='helpdesk.team',
        relation='helpdesk_team_users_rel',
        column1='user_id',
        column2='team_id',
        string='Helpdesk Teams')

