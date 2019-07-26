# Generated by Django 2.2 on 2019-07-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_presentation_is_breaktime'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='is_breaktime',
            field=models.BooleanField(default=False, help_text='쉬는 시간일 경우 TRUE로 설정합니다.'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='is_breaktime',
            field=models.BooleanField(default=False, help_text='쉬는 시간일 경우 TRUE로 설정합니다.'),
        ),
    ]