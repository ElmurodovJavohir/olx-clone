# Generated by Django 4.2.6 on 2023-11-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_attributeoption_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='filter_type',
            field=models.CharField(choices=[('range', 'Range'), ('multiselect', 'Multiselect')], default='range', max_length=255),
        ),
        migrations.AddField(
            model_name='attribute',
            name='is_filter',
            field=models.BooleanField(default=False),
        ),
    ]
