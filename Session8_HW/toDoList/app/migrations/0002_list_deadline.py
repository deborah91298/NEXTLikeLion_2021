# Generated by Django 3.2.2 on 2021-05-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
