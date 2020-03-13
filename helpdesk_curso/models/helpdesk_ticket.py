from odoo import api, fields, models, _

class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'

    _inherit = ['mail.thread.cc', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')

    tickets_qty = fields.Integer(string="Tickets qty", compute="_compute_tickets_qty")

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
    def onchange_method_users(self):
        self.user_ids = self.team_id.user_ids

    @api.onchange('name', 'date_deadline')
    def onchange_method_description(self):
        if self.name and self.date_deadline:
            self.description = "%s - %s"%(self.name, self.date_deadline)
        #self.description = self.name + self.date_deadline

    @api.depends('responsable_id')
    def _compute_tickets_qty(self):
        #debug por terminal: l, n, ...
        import pdb; pdb.set_trace();
        #debug por web?: buscar por inet, hay que instalar cliente y servidor. Avanzado.
        #import wdb; wdb.set_trace();
        ticket_obj = self.env['helpdesk.ticket']
        for ticket in self:
            # A o B o C -> (A o B) o C -> o (A, B) o C -> oo ((A, B), C)
            tickets = ticket_obj.search([
                '|',
                    '|',
                        ('responsable_id', '=', ticket.responsable_id.id),
                        ('responsable_id', '=', False),
                    ('stage_id', '=', ticket.stage_id.id)])
            ticket.tickets_qty = len(tickets)


    def set_responsable(self):
        self.ensure_one()
        self.responsable_id = self.env.user
        # Haría lo mismo pero con un solo acceso a bbdd si hubiese más de un campo a cambiar
        #self.write({'responsable_id': self.env.user})
