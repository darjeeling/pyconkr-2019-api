# Generated by Django 2.2 on 2019-08-13 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0085_lightningtalk_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='material',
        ),
    ]
