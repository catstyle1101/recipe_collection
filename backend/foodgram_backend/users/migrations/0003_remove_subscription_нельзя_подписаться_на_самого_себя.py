# Generated by Django 4.2.1 on 2023-06-10 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_subscription_subscription_нельзя_подписаться_дважды_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='subscription',
            name='Нельзя подписаться на самого себя',
        ),
    ]
