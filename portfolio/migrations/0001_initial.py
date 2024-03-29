# Generated by Django 3.2 on 2023-09-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Project Name')),
                ('description', models.TextField(verbose_name="Projects's description")),
                ('link', models.CharField(blank=True, max_length=256, null=True, verbose_name='Link to Project')),
                ('github', models.CharField(blank=True, max_length=256, null=True, verbose_name='Github Link')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/porfolio/%Y_%m_%d')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/porfolio/%Y_%m_%d')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/porfolio/%Y_%m_%d')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='media/porfolio/%Y_%m_%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
