# Generated by Django 3.0.6 on 2020-05-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renderringAndModels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]