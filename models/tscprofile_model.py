# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TSCProfile(models.Model):
    _name = 'tsc.profile'
    _description = 'TSC Team'

    position_choice = [
        ('Leader','Leader'),
        ('Advisor','Advisor'),
        ('Researcher','Researcher'),
        ('Engineer','Engineer')
    ]

    name = fields.Char(string='Name in TSC', required=True)
    position = fields.Selection(position_choice,string='Position in TSC',required=True)
    position_detail = fields.Char(string='Position detail', required=True)
    organization = fields.Char(string='Your Organization',required=True)
    email = fields.Char(string='Email')
    date_join = fields.Datetime(string='Date joined')
    img = fields.Image(string='Your image',
                       max_width=200, max_height=200)


