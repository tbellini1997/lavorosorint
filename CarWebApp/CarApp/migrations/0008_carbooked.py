# Generated by Django 2.0.4 on 2018-05-19 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarApp', '0007_car_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarApp.Car')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarApp.User')),
            ],
        ),
    ]
