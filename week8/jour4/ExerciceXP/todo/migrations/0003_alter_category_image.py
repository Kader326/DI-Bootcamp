# Generated by Django 4.1.3 on 2022-11-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0002_alter_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
