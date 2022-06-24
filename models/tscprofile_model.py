# -*- coding: utf-8 -*-

from odoo import models, fields

class TSCProfile(models.Model):
    _name = 'tsc.profile'

    name = fields.Char(String="Name in TSC", require=True)
    position = fields.Char(String="Position in TSC",require=True)
    organization = fields.Char(String="Your Organization",require=True)
    email = fields.Char(String="Email")
    date_join = fields.Datetime(String="Date joined")
    img = fields.Image(String="Your image",require=True)

