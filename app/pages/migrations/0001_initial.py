# Generated by Django 3.0.7 on 2020-06-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(max_length=120, verbose_name='Тег title')),
                ('seo_description', models.CharField(max_length=120, verbose_name='Тег description')),
                ('title', models.CharField(max_length=350, verbose_name='Заголовок')),
                ('menu_title', models.CharField(max_length=120, verbose_name='Заголовок в меню')),
                ('slug', models.SlugField(unique=True, verbose_name='Урл')),
                ('content', models.TextField(blank=True, verbose_name='Содержимое')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'unique_together': {('slug',)},
            },
        ),
    ]
