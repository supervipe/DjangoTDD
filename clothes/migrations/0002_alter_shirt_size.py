# Generated by Django 4.1 on 2022-08-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='size',
            field=models.CharField(max_length=255),
        ),
    ]
