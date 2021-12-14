# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit='res.partner'

    instructor=fields.Boolean(default=False)
    session_ids=fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)
    otherfield=fields.Boolean(default=True, string="Other Field")
    otherfield2=fields.Boolean(default=True, string="Other Field 2")
