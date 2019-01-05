# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields


class AgreementCancelAgreement(models.TransientModel):
    _name = "agreement.cancel_agreement"
    _description = "Cancel Agreement"

    cancel_reason_id = fields.Many2one(
        string="Cancel Reason",
        comodel_name="agreement.cancel_reason",
        required=True,
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._confirm_cancel()

    @api.multi
    def _confirm_cancel(self):
        self.ensure_one()
        agreement_ids = self.env.context.get("active_ids", [])
        agreements = self.env["agreement.agreement"].browse(
            agreement_ids
        )
        agreements.button_cancel(self.cancel_reason_id.id)
