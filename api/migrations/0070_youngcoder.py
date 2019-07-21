# Generated by Django 2.2 on 2019-07-21 08:28

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_auto_20190708_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoungCoder',
            fields=[
                ('program_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Program')),
                ('num_of_participants', models.IntegerField(default=0, help_text='수강 적절 인원 수 입니다.')),
                ('company_name', models.CharField(blank=True, default='', max_length=64)),
                ('company_name_ko', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('company_name_en', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('company_logo', sorl.thumbnail.fields.ImageField(blank=True, default='', upload_to='profile')),
                ('company_desc', models.TextField(blank=True, default='')),
                ('company_desc_ko', models.TextField(blank=True, default='', null=True)),
                ('company_desc_en', models.TextField(blank=True, default='', null=True)),
                ('recommend_age', models.CharField(blank=True, default='10세 이상', max_length=64)),
                ('recommend_age_ko', models.CharField(blank=True, default='10세 이상', max_length=64, null=True)),
                ('recommend_age_en', models.CharField(blank=True, default='10세 이상', max_length=64, null=True)),
            ],
            bases=('api.program',),
        ),
    ]
