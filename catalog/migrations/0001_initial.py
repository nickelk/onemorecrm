# Generated by Django 3.2.9 on 2021-12-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter email', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='Enter phone number', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='Enter company name', max_length=300)),
                ('foreman_name', models.CharField(help_text="Enter foreman's name", max_length=300)),
                ('descriptions', models.TextField(help_text='Describe the company')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('date_of_edition', models.DateField(auto_now=True)),
                ('adress', models.CharField(help_text='Enter the adress of the organization', max_length=300)),
                ('email', models.ManyToManyField(help_text='Select email', to='catalog.Email')),
                ('phone', models.ManyToManyField(help_text='Select phone number', to='catalog.Phone')),
            ],
        ),
    ]
