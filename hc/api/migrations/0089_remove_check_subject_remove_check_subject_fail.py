# Generated by Django 4.0.6 on 2022-07-13 08:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0088_fill_kw"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="check",
            name="subject",
        ),
        migrations.RemoveField(
            model_name="check",
            name="subject_fail",
        ),
    ]
