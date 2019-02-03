# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AgreementPartyAbstract(models.AbstractModel):
    _name = "agreement.party_abstract"
    _description = "Abstract Model for Agreement Party"
    _order = "sequence, id"

    agreement_id = fields.Many2one(
        string="Agreement",
        comodel_name="agreement.abstract",
        required=True,
        index=True,
        ondelete="cascade",
    )
    name = fields.Char(
        string="Party Alias",
        required=True,
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
        required=True,
    )
    party_id = fields.Many2one(
        string="Party",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
        ],
    )
    contact_id = fields.Many2one(
        string="Contact",
        comodel_name="res.partner",
        domain=[
            ("parent_id", "=", False),
            ("is_company", "=", False),
        ],
    )
