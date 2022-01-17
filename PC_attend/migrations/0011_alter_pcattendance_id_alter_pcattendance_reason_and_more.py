# Generated by Django 4.0 on 2022-01-15 19:37

import PC_attend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_attend', '0010_auto_20220114_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcattendance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pcattendance',
            name='reason',
            field=models.CharField(blank=True, choices=[('Out of Town', 'Out of Town'), ('Sick', 'Sick'), ('Not_available', 'Not available')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pcattendance',
            name='service_date',
            field=models.DateField(help_text='Enter the date of Service', validators=[PC_attend.models.no_future]),
        ),
    ]