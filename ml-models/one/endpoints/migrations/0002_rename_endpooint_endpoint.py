# Generated by Django 4.1.7 on 2023-03-05 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("endpoints", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Endpooint",
            new_name="Endpoint",
        ),
    ]
