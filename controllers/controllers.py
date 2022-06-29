# -*- coding: utf-8 -*-
from odoo import http

class tscprofile(http.Controller):
    @http.route('/team', auth='public', website=True)
    def index(self, **kw):
        leader_team = http.request.env['tsc.profile'].search([('position', '=', 'Leader')])
        advisor_team = http.request.env['tsc.profile'].search([('position', '=', 'Advisor')])
        researcher_team = http.request.env['tsc.profile'].search([('position', '=', 'Researcher')])
        engineer_team = http.request.env['tsc.profile'].search([('position', '=', 'Engineer')])
        return http.request.render("tscprofile.namelist",{
            'leader_team':leader_team,
            'advisor_team':advisor_team,
            'researcher_team':researcher_team,
            'engineer_team':engineer_team,
        })