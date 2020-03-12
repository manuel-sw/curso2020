from odoo import api, fields, models, _

class HelpdeskSetResponsable(models.TransientModel):
    _name = "helpdesk.set.responsable"

    tickets_qty = fields.Integer(string="Tickets qty")

    @api.model
    def default_get(self, fields):
        res = super(HelpdeskSetResponsable, self).default_get(fields)
        user_id = self.env.uid
        tickets = self.env['helpdesk.ticket'].search([('responsable_id', '=', user_id)])
        res['tickets_qty'] = len(tickets)
        return res
    
    def set_responsable(self):
        self.ensure_one()
        print("context:", self.env.context)
        active_id = self.env.context.get('active_id')
        if (active_id):
            ticket = self.env['helpdesk.ticket'].browse(active_id)
            if (ticket):
                ticket.responsable_id = self.env.user