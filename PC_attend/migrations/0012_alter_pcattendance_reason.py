# Generated by Django 4.0 on 2022-01-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_attend', '0011_alter_pcattendance_id_alter_pcattendance_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcattendance',
            name='reason',
            field=models.CharField(blank=True, choices=[('Out of Town', 'Out of Town'), ('Not_available', 'Not available'), ('Sick', 'Sick')], max_length=100),
        ),
    ]