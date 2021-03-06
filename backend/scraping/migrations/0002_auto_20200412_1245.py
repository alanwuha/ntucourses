# Generated by Django 3.0.5 on 2020-04-12 04:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_type',
            field=models.CharField(blank=True, choices=[('LEC', 'Lecture'), ('TUT', 'Tutorial'), ('LAB', 'Laboratory'), ('SEM', 'Seminar'), ('PRJ', 'Project'), ('DES', 'Design')], max_length=3),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(default='SYSTEM', max_length=20)),
                ('last_updated_datetime', models.DateTimeField(auto_now=True)),
                ('last_updated_by', models.CharField(default='SYSTEM', max_length=20)),
                ('date', models.DateField()),
                ('day', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=3)),
                ('time', models.TimeField()),
                ('duration', models.FloatField()),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2019), django.core.validators.MaxValueValidator(9999)])),
                ('semester', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('course_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scraping.Course')),
            ],
        ),
        migrations.AddConstraint(
            model_name='exam',
            constraint=models.UniqueConstraint(fields=('course_code', 'year', 'semester'), name='unique_exam'),
        ),
    ]
