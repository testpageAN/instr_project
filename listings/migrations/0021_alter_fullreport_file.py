# Generated by Django 4.1.5 on 2023-02-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0020_alter_fullreport_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fullreport",
            name="file",
            field=models.FileField(
                blank=True,
                max_length=255,
                upload_to="reports_files/%Y/%m/%d/",
                verbose_name="Files",
            ),
        ),
    ]
