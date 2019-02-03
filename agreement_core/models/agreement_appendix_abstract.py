# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AgreementAppendixAbstract(models.AbstractModel):
    _name = "agreement.appendix_abstract"
    _description = "Abstract Model for Agreement Appendix"
    _order = "sequence, id"

    @api.multi
    @api.depends(
        "raw_content",
    )
    def _compute_content(self):
        MailTemplate = self.env["mail.template"]
        for appendix in self:
            # lang = appendix.agreement_id.lang or "en_US"
            lang = "en_US"
            result = "-"
            if type(appendix.id) is int:
                try:
                    result = MailTemplate.with_context(lang=lang).\
                        render_template(
                            appendix.raw_content,
                            str(appendix._name),
                            appendix.id)
                except:
                    pass
            appendix.content = result

    agreement_id = fields.Many2one(
        string="Agreement",
        comodel_name="agreement.abstract",
        required=True,
        index=True,
        ondelete="cascade",
    )
    name = fields.Char(
        string="Appendix",
        required=True,
    )
    title = fields.Char(
        string="Title",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=5,
        required=True,
    )
    raw_content = fields.Text(
        string="Raw Content",
    )
    content = fields.Text(
        string="Content",
        compute="_compute_content",
        store=False,
    )
