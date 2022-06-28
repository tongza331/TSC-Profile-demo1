# -*- coding: utf-8 -*-
from odoo import http

class tscprofile(http.Controller):
    @http.route('/team', auth='public', website=True)
    def index(self, **kw):
        our_team = http.request.env['tsc.profile'].sudo().search([])
        return http.request.render("tscprofile.namelist",{
            'team':our_team,
        })