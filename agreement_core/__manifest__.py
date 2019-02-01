# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Agreement - Core",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "depends": [
        "base_sequence_configurator",
        "base_workflow_policy",
        "mail",
        "base_document_version",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "menu.xml",
        "wizards/cancel_agreement.xml",
        "wizards/terminate_agreement.xml",
        "wizards/attach_signed_document.xml",
        "views/agreement_config_setting_views.xml",
        "views/agreement_type_views.xml",
        "views/agreement_template_views.xml",
        "views/agreement_agreement_views.xml",
        "views/agreement_cancel_reason_views.xml",
        "views/agreement_termination_reason_views.xml",
    ],
}
