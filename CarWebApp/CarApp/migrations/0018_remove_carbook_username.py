# Generated by Django 2.0.4 on 2018-05-19 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0017_auto_20180519_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbook',
            name='username',
        ),
    ]
