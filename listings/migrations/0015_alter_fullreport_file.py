# Generated by Django 4.1.5 on 2023-01-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0014_alter_fullreport_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fullreport",
            name="file",
            field=models.FileField(
                blank=True,
                storage="reports_files/%Y/%m/%d/",
                upload_to="",
                verbose_name="Files",
            ),
        ),
    ]
