# Generated by Django 3.2 on 2023-03-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='upated',
            new_name='updated',
        ),
    ]