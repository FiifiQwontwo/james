# Generated by Django 3.2.11 on 2022-01-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PC_attend', '0016_alter_pcattendance_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcattendance',
            name='reason',
            field=models.CharField(blank=True, choices=[('No_idea', 'No Idea'), ('No_reason', 'No reason'), ('Out of Town', 'Out of Town'), ('relocated', 'relocated'), ('Sick', 'Sick')], max_length=100),
        ),
    ]
