# Generated by Django 4.0 on 2021-12-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_attend', '0005_alter_pcattendance_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcattendance',
            name='reason',
            field=models.CharField(choices=[('Not_available', 'Not available'), ('Sick', 'Sick'), ('Out of Town', 'Out of Town')], max_length=100),
        ),
    ]