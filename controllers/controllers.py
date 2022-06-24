# -*- coding: utf-8 -*-
from odoo import http

class tscprofile(http.Controller):
    @http.route('/team', auth='public', website=True)
    def index(self, **kw):
        try:
            our_team = http.request.env['tsc.profile'].search([])

        except:
            return "<h1>Can't Access API</h1>"

        return http.request.render("tscprofile.namelist",{
            'team':our_team,
        })