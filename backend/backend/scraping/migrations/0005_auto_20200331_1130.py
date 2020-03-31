# Generated by Django 3.0.4 on 2020-03-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20200330_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['course_code']},
        ),
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.CharField(default='system', max_length=20),
        ),
        migrations.AddField(
            model_name='course',
            name='grade_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='last_updated_by',
            field=models.CharField(default='system', max_length=20),
        ),
        migrations.AddField(
            model_name='course',
            name='mutually_exclusive_with',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='not_available_as_core_to_programme',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='not_available_as_pe_to_programme',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='not_available_as_ue_to_programme',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='not_available_to_all_programme_with',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='not_available_to_programme',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisite',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
