# Generated by Django 4.2.6 on 2023-10-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_signin_name_alter_signin_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='phone',
            field=models.TextField(),
        ),
    ]
