# Generated by Django 3.2 on 2023-09-15 01:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_common'),
    ]

    operations = [
        migrations.AddField(
            model_name='common',
            name='about_headline',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]