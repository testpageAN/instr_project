# Generated by Django 4.1.5 on 2023-01-28 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0008_listing_file_delete_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="file",
        ),
    ]
