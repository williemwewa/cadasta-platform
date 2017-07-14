# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('organization', '0004_remove_Pb_project_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorganizationrole',
            name='group',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='historicalprojectrole',
            name='group',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='organizationrole',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_roles', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='projectrole',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_roles', to='auth.Group'),
        ),
    ]