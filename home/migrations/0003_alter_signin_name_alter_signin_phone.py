# Generated by Django 4.2.6 on 2023-10-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contact_signin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='signin',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
