# Generated by Django 2.0.4 on 2018-05-19 15:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0015_auto_20180519_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frombooked', models.DateField(default=datetime.date.today)),
                ('tobooked', models.DateField(default=datetime.date.today)),
                ('note', models.TextField(default='Aggiungi note..')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarApp.Car')),
                ('username', models.ManyToManyField(to='CarApp.User')),
            ],
        ),
    ]
