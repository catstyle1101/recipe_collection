# Generated by Django 4.2.1 on 2023-06-11 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_subscription_нельзя_подписаться_на_самого_себя'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
