# Generated by Django 2.0 on 2018-01-17 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0025_auto_20180117_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 19, 14, 50, 8, 243000, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
