# Generated by Django 4.2 on 2023-04-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='facilitator',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
