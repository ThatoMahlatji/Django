# Generated by Django 4.1.5 on 2023-02-03 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="list_date",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
