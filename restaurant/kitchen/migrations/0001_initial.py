# Generated by Django 4.2.4 on 2023-09-27 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='')),
                ('description', models.TextField(default='Описание блюда', verbose_name='Описание блюда')),
            ],
            options={
                'verbose_name': 'Кухня',
                'verbose_name_plural': 'Кухни',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('description', models.TextField(default='Описание', verbose_name='Описание')),
                ('price', models.FloatField()),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='kitchen.meal', verbose_name='Блюдо')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категория блюда')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='Слаг')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='kitchen.category', verbose_name='Принадлежит к')),
            ],
            options={
                'verbose_name': 'Категория блюда',
                'verbose_name_plural': 'Категории блюд',
            },
        ),
    ]
