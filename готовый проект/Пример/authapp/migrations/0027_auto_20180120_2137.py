# Generated by Django 2.0 on 2018-01-20 16:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0026_auto_20180117_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 22, 16, 37, 43, 539550, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
