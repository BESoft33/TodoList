# Generated by Django 3.0.8 on 2020-08-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]