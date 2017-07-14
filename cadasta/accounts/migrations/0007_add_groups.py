# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-03 15:57
from __future__ import unicode_literals

from django.db import migrations


def create_groups(apps, schema_editor):
    groups = ['SuperUser', 'OrgAdmin', 'OrgMember', 'ProjectManager',
              'DataCollector', 'ProjectMember', 'PublicUser', 'AnonymousUser']
    Group = apps.get_model("auth", "Group")
    for group in groups:
        Group.objects.create(name=group)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_add_measurement_field'),
    ]

    operations = [
        migrations.RunPython(create_groups, migrations.RunPython.noop),
    ]