# Generated by Django 4.2.3 on 2023-08-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_5', '0003_alter_advertisement_date_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='date_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
