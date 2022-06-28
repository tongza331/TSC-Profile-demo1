# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TSCProfile(models.Model):
    _name = 'tsc.profile'
    _description = 'TSC Team'

    name = fields.Char(string="Name in TSC", required=True)
    position = fields.Char(string="Position in TSC",required=True)
    organization = fields.Char(string="Your Organization",required=True)
    email = fields.Char(string="Email")
    date_join = fields.Datetime(string="Date joined")
    img = fields.Image(string="Your image",required=True,
                       max_width = 200, max_height = 200)

