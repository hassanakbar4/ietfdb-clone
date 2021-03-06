# Generated by Django 2.2.14 on 2020-07-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0012_auto_20200624_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalperson',
            name='plain',
            field=models.CharField(blank=True, default='', help_text='Preferred plain form of name, if different from the automatic plain form.', max_length=64, verbose_name='Plain Name (Unicode)'),
        ),
        migrations.AddField(
            model_name='person',
            name='plain',
            field=models.CharField(blank=True, default='', help_text='Preferred plain form of name, if different from the automatic plain form.', max_length=64, verbose_name='Plain Name (Unicode)'),
        ),
        migrations.AlterField(
            model_name='historicalperson',
            name='name',
            field=models.CharField(db_index=True, help_text='Preferred long form of name.', max_length=255, verbose_name='Full Name (Unicode)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(db_index=True, help_text='Preferred long form of name.', max_length=255, verbose_name='Full Name (Unicode)'),
        ),
    ]
