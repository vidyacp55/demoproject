# Generated by Django 3.2.20 on 2023-08-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-23'),
            preserve_default=False,
        ),
    ]