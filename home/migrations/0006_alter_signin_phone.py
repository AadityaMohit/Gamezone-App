# Generated by Django 4.2.6 on 2023-10-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_signin_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
