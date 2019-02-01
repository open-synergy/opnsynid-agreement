# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AgreementAgreementClause(models.Model):
    _name = "agreement.agreement_clause"
    _description = "Agreement Clause"
    _inherit = "agreement.clause_abstract"

    section_id = fields.Many2one(
        comodel_name="agreement.agreement_section",
    )
