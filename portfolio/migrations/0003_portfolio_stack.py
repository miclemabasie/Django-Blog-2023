# Generated by Django 3.2 on 2023-09-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20230910_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='stack',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
