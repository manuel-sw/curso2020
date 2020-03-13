from odoo.tests.common import SavepointCase

class HelpdeskCase(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.team_obj = cls.env['helpdesk.team']
        cls.ticket_obj = cls.env['helpdesk.ticket']
        cls.ticket_stage_obj = cls.env['helpdesk.ticket.stage']
        cls.user_obj = cls.env['res.users']

        cls.user_demo = cls.env.ref['base.user_demo']
        cls.user_admin = cls.env.ref['base.user_admin']

    def test_create_ticket(self):
        ticket = self.ticket_obj.create({
            #'name': 'test ticket',
            'responsable_id': self.user_demo.id
        })