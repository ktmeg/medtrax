# Generated by Django 3.0.5 on 2020-05-12 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200512_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meds',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meds',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]