# Generated by Django 3.0.5 on 2020-04-12 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0008_auto_20200412_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='class',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Course'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Course'),
        ),
    ]
