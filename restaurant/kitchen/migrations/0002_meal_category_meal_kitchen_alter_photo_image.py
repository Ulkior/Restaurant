# Generated by Django 4.2.4 on 2023-09-27 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='meal', to='kitchen.category', verbose_name='Категория продукта'),
        ),
        migrations.AddField(
            model_name='meal',
            name='kitchen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kitchen.kitchen', verbose_name='Кухня продукта'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='meal/'),
        ),
    ]
