# Generated by Django 2.2.14 on 2020-07-28 09:30

from django.db import migrations

def forward(apps, schema_editor):
    GroupFeatures = apps.get_model('group','GroupFeatures')
    GroupFeatures.objects.create(
        about_page = 'ietf.group.views.group_about',
        acts_like_wg = True,
        admin_roles = ['chair'],
        agenda_type_id = 'ietf',
        create_wiki = True,
        custom_group_roles = True,
        customize_workflow = False,
        default_tab = 'ietf.group.views.group_about',
        default_used_roles = ['chair', 'secr'],
        docman_roles = ['chair', 'delegate', 'secr'],
        groupman_authroles = ['Secretariat', 'IRTF Chair'],
        groupman_roles = ['chair', 'delegate'],
        has_chartering_process = False,
        has_default_jabber = False,
        has_documents = True,
        has_meetings = True,
        has_milestones = False,
        has_nonsession_materials = False,
        has_reviews = False,
        has_session_materials = True,
        is_schedulable = True,
        material_types = ['slides'],
        matman_roles = ['chair', 'delegate', 'secr'],
        req_subm_approval = True,
        role_order = ['chair', 'secr'],
        show_on_agenda = True,
        type_id = 'rag',
    )

    Group = apps.get_model('group','Group')
    Group.objects.filter(type_id='ag',parent__acronym='irtf').update(type_id='rag')

def reverse(apps, schema_editor):
    Group = apps.get_model('group','Group')
    Group.objects.filter(type_id='rag',parent__acronym='irtf').update(type_id='ag')

    GroupFeatures = apps.get_model('group','GroupFeatures')
    GroupFeatures.objects.filter(type_id='rag').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('group', '0034_populate_groupextresources'),
        ('name', '0016_add_research_area_groups'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]
