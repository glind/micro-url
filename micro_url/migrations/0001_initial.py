# Generated by Django 2.1.5 on 2019-05-31 11:52

from django.db import migrations, models
import micro_url.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLService',
            fields=[
                ('original_url', models.CharField(help_text='Old Long URL.', max_length=255)),
                ('new_url', models.CharField(help_text='New Shorty URL.', max_length=255)),
                ('unique_id', models.CharField(help_text='Unique ID', max_length=55, primary_key=True, serialize=False)),
                ('count', models.IntegerField(help_text='Number of times used')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the URL was created (automatically set, ISO format).')),
                ('edit_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the URL was last modified (automatically set, ISO format).')),
            ],
        ),
    ]