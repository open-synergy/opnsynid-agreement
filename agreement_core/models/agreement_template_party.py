# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AgreementTemplateParty(models.Model):
    _name = "agreement.template_party"
    _description = "Agreement Template Party"
    _inherit = "agreement.party_abstract"

    agreement_id = fields.Many2one(
        comodel_name="agreement.template",
    )
