# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResConfig(models.TransientModel):
    _name = "agreement.config_setting"
    _inherit = "res.config.settings"

    agreement_confirm_group_ids = fields.Many2many(
        string="Allow To Confirm Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_confirm_group_ids",
        readonly=False,
    )
    agreement_print_group_ids = fields.Many2many(
        string="Allow To Print Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_print_group_ids",
        readonly=False,
    )
    agreement_attach_group_ids = fields.Many2many(
        string="Allow To Attach Signed Document",
        comodel_name="res.groups",
        related="company_id.agreement_attach_group_ids",
        readonly=False,
    )
    agreement_approve_group_ids = fields.Many2many(
        string="Allow To Approve Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_approve_group_ids",
        readonly=False,
    )
    agreement_active_group_ids = fields.Many2many(
        string="Allow To Activate Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_active_group_ids",
        readonly=False,
    )
    agreement_expire_group_ids = fields.Many2many(
        string="Allow To Mark As Expire Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_expire_group_ids",
        readonly=False,
    )
    agreement_terminate_group_ids = fields.Many2many(
        string="Allow To Terminate Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_terminate_group_ids",
        readonly=False,
    )
    agreement_revision_group_ids = fields.Many2many(
        string="Allow To Create New Revision",
        comodel_name="res.groups",
        related="company_id.agreement_revision_group_ids",
        readonly=False,
    )
    agreement_cancel_group_ids = fields.Many2many(
        string="Allow To Cancel Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_cancel_group_ids",
        readonly=False,
    )
    agreement_restart_group_ids = fields.Many2many(
        string="Allow To Restart Agreement",
        comodel_name="res.groups",
        related="company_id.agreement_restart_group_ids",
        readonly=False,
    )
