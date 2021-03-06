# Generated by Django 3.2.9 on 2021-12-05 08:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20211204_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='grade',
            field=models.DecimalField(blank=True, choices=[(-5, '-5'), (-4, '-4'), (-3, '-3'), (-2, '-2'), (-1, '-1'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], decimal_places=1, default=1, help_text='Interaction grade', max_digits=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
