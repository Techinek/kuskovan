# Generated by Django 3.0.7 on 2020-06-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=120, verbose_name='Тема'),
        ),
    ]
