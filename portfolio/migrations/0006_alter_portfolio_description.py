# Generated by Django 3.2 on 2023-09-14 01:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfolio_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
