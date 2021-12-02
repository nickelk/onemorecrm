# Generated by Django 3.2.9 on 2021-12-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20211202_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.ManyToManyField(help_text='Enter email', to='catalog.Email'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.ManyToManyField(help_text='Enter phone number', to='catalog.Phone'),
        ),
    ]
