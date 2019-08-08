# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 04:43


from __future__ import absolute_import, print_function, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0011_reviewassignmentdocevent'),
        # present to facilitate migration to just before reveiw.0010:
        ('name', '0006_adjust_statenames'), 
        ('dbtemplate', '0004_adjust_assignment_email_summary_templates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docevent',
            name='type',
            field=models.CharField(choices=[('new_revision', 'Added new revision'), ('new_submission', 'Uploaded new revision'), ('changed_document', 'Changed document metadata'), ('added_comment', 'Added comment'), ('added_message', 'Added message'), ('edited_authors', 'Edited the documents author list'), ('deleted', 'Deleted document'), ('changed_state', 'Changed state'), ('changed_stream', 'Changed document stream'), ('expired_document', 'Expired document'), ('extended_expiry', 'Extended expiry of document'), ('requested_resurrect', 'Requested resurrect'), ('completed_resurrect', 'Completed resurrect'), ('changed_consensus', 'Changed consensus'), ('published_rfc', 'Published RFC'), ('added_suggested_replaces', 'Added suggested replacement relationships'), ('reviewed_suggested_replaces', 'Reviewed suggested replacement relationships'), ('changed_group', 'Changed group'), ('changed_protocol_writeup', 'Changed protocol writeup'), ('changed_charter_milestone', 'Changed charter milestone'), ('initial_review', 'Set initial review time'), ('changed_review_announcement', 'Changed WG Review text'), ('changed_action_announcement', 'Changed WG Action text'), ('started_iesg_process', 'Started IESG process on document'), ('created_ballot', 'Created ballot'), ('closed_ballot', 'Closed ballot'), ('sent_ballot_announcement', 'Sent ballot announcement'), ('changed_ballot_position', 'Changed ballot position'), ('changed_ballot_approval_text', 'Changed ballot approval text'), ('changed_ballot_writeup_text', 'Changed ballot writeup text'), ('changed_rfc_editor_note_text', 'Changed RFC Editor Note text'), ('changed_last_call_text', 'Changed last call text'), ('requested_last_call', 'Requested last call'), ('sent_last_call', 'Sent last call'), ('scheduled_for_telechat', 'Scheduled for telechat'), ('iesg_approved', 'IESG approved document (no problem)'), ('iesg_disapproved', 'IESG disapproved document (do not publish)'), ('approved_in_minute', 'Approved in minute'), ('iana_review', 'IANA review comment'), ('rfc_in_iana_registry', 'RFC is in IANA registry'), ('rfc_editor_received_announcement', 'Announcement was received by RFC Editor'), ('requested_publication', 'Publication at RFC Editor requested'), ('sync_from_rfc_editor', 'Received updated information from RFC Editor'), ('requested_review', 'Requested review'), ('assigned_review_request', 'Assigned review request'), ('closed_review_request', 'Closed review request'), ('closed_review_assignment', 'Closed review assignment'), ('downref_approved', 'Downref approved')], max_length=50),
        ),
    ]
