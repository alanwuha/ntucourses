# Generated by Django 3.0.5 on 2020-05-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0012_auto_20200513_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['course_code_id', '-year', '-semester', 'index', 'class_type', 'group', 'day', 'start_time', 'end_time']},
        ),
        migrations.RemoveConstraint(
            model_name='class',
            name='unique_class',
        ),
        migrations.AddField(
            model_name='class',
            name='index',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddConstraint(
            model_name='class',
            constraint=models.UniqueConstraint(fields=('index', 'class_type', 'group', 'day', 'start_time', 'end_time', 'venue', 'remark', 'course_code_id', 'year', 'semester'), name='unique_class'),
        ),
    ]