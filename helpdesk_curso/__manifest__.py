{
    'name': "HelpDesk Curso",
    'summary':
        "Module to support teams",
    'version': '13.0.1.0',
    'category': 'Customer relationship management',
    'website': "",
    'author': "manuel-sw",
    'license' : "AGPL-3",
    'data': [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "wizard/helpdesk_set_responsable_view.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_ticket_stage_views.xml",
        "views/helpdesk_team_views.xml",
        "views/res_users_views.xml",
        "views/menus.xml",

    ],
    'application': True,
    'installable': True,
    'depends': [
            "base",
            "mail",
    ],
}
