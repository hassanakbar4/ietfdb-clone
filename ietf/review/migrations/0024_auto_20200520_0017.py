# Generated by Django 2.0.13 on 2020-05-20 00:17

from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0023_historicalreviewersettings_change_reason_text_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='team',
            field=ietf.utils.models.ForeignKey(blank=True, db_constraint=False, limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='group.Group'),
        ),
        migrations.AlterField(
            model_name='historicalreviewrequest',
            name='team',
            field=ietf.utils.models.ForeignKey(blank=True, db_constraint=False, limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='group.Group'),
        ),
        migrations.AlterField(
            model_name='historicalunavailableperiod',
            name='team',
            field=ietf.utils.models.ForeignKey(blank=True, db_constraint=False, limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='group.Group'),
        ),
        migrations.AlterField(
            model_name='nextreviewerinteam',
            name='team',
            field=ietf.utils.models.ForeignKey(limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='team',
            field=ietf.utils.models.ForeignKey(limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
        migrations.AlterField(
            model_name='reviewrequest',
            name='team',
            field=ietf.utils.models.ForeignKey(limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
        migrations.AlterField(
            model_name='reviewsecretarysettings',
            name='team',
            field=ietf.utils.models.ForeignKey(limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
        migrations.AlterField(
            model_name='reviewwish',
            name='team',
            field=ietf.utils.models.ForeignKey(limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
        migrations.AlterField(
            model_name='unavailableperiod',
            name='team',
            field=ietf.utils.models.ForeignKey(limit_choices_to=models.Q(_negated=True, reviewteamsettings=None), on_delete=django.db.models.deletion.CASCADE, to='group.Group'),
        ),
    ]
