# Generated by Django 2.2 on 2019-08-04 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0077_auto_20190729_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightningTalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('accepted', models.BooleanField(default=True)),
                ('material', models.FileField(blank=True, default='', upload_to='lightningtalk')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
