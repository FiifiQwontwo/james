# Generated by Django 4.0 on 2022-01-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_attend', '0012_alter_pcattendance_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcattendance',
            name='reason',
            field=models.CharField(blank=True, choices=[('Out of Town', 'Out of Town'), ('Sick', 'Sick'), ('Not_available', 'Not available')], max_length=100),
        ),
    ]
