# Generated by Django 2.2.20 on 2021-05-05 10:05

from collections import namedtuple
from django.db import migrations
from django.db.models import Max


# Simple type for representing constraint name data that will be
# modified.
ConstraintInfo = namedtuple(
    'ConstraintInfo',
    ['replaces', 'slug', 'name', 'desc', 'editor_label'],
)

constraint_names_to_add = [
    ConstraintInfo(
        replaces='conflict',
        slug='chair_conflict',
        name='Chair conflict',
        desc='Indicates other WGs the chairs also lead or will be active participants in',
        editor_label='<i class="fa fa-gavel"></i>',
    ),
    ConstraintInfo(
        replaces='conflic2',
        slug='tech_overlap',
        name='Technology overlap',
        desc='Indicates WGs with a related technology or a closely related charter',
        editor_label='<i class="fa fa-rocket"></i>',
    ),
    ConstraintInfo(
        replaces='conflic3',
        slug='key_participant',
        name='Key participant conflict',
        desc='Indicates WGs with which key participants (presenter, secretary, etc.)  may overlap',
        editor_label='<i class="fa fa-key"></i>',
    )
]


def forward(apps, schema_editor):
    ConstraintName = apps.get_model('name', 'ConstraintName')
    max_order = ConstraintName.objects.all().aggregate(Max('order'))['order__max']

    for index, new_constraint in enumerate(constraint_names_to_add):
        # hack_constraint is the constraint type relabeled by the hack fix in #2754
        hack_constraint = ConstraintName.objects.get(slug=new_constraint.replaces)
        ConstraintName.objects.create(
            slug=new_constraint.slug,
            name=new_constraint.name,
            desc=new_constraint.desc,
            used=hack_constraint.used,
            order=max_order + index + 1,
            penalty=hack_constraint.penalty,
            editor_label=new_constraint.editor_label,
            is_group_conflict=True,
        )


def reverse(apps, schema_editor):
    ConstraintName = apps.get_model('name', 'ConstraintName')
    for new_constraint in constraint_names_to_add:
        ConstraintName.objects.filter(slug=new_constraint.slug).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('name', '0025_set_constraintname_is_group_conflict'),
        # Reversing this migration requires that the 'day' field be removed from
        # the Constraint model, so we indirectly depend on the migration that
        # removed it.
        ('meeting', '0027_add_constraint_options_and_joint_groups'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
