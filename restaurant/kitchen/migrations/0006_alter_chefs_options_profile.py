# Generated by Django 4.2.4 on 2023-10-08 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitchen', '0005_chefs_events_alter_kitchen_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chefs',
            options={'verbose_name': 'Повар', 'verbose_name_plural': 'Повара'},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(default='Unemployed', max_length=255, verbose_name='Профессия')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='photos/profiles/', verbose_name='Фото')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('bio', models.CharField(default='Инфо о себе', max_length=255, verbose_name='Био')),
                ('city', models.CharField(default='Город', max_length=255, verbose_name='City...')),
                ('region', models.CharField(default='Штат/Регион', max_length=255, verbose_name='State/Region')),
                ('instagram', models.CharField(default='@username', max_length=255, verbose_name='Инстаграм')),
                ('telegram', models.CharField(default='@username', max_length=255, verbose_name='Телеграм')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
