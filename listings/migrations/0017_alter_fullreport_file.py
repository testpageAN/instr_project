# Generated by Django 4.1.5 on 2023-01-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0016_alter_fullreport_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fullreport",
            name="file",
            field=models.FileField(
                blank=True, upload_to="reports_files/%Y/%m/%d/", verbose_name="Files"
            ),
        ),
    ]
