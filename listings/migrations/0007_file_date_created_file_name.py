# Generated by Django 4.1.5 on 2023-01-27 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0006_alter_file_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="date_created",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="file",
            name="name",
            field=models.CharField(auto_created=True, default=1, max_length=50),
            preserve_default=False,
        ),
    ]
