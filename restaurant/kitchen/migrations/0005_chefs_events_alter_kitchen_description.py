# Generated by Django 4.2.4 on 2023-10-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_alter_kitchen_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя повара')),
                ('chef_title', models.CharField(max_length=100, verbose_name='Звание повара')),
                ('image', models.ImageField(upload_to='photos/chefs/')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование событий')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('description', models.TextField(default='Подробности', verbose_name='Подробно о услугах')),
                ('image', models.ImageField(upload_to='photos/events/')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='description',
            field=models.TextField(default='Описание кухни', verbose_name='Описание кухни'),
        ),
    ]
