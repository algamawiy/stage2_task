# Generated by Django 4.1.3 on 2022-11-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arithmetic_operator', '0004_alter_arithmetic_operation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arithmetic',
            name='operation_type',
            field=models.CharField(choices=[('addition', 'addition'), ('subtraction', 'subtraction'), ('multiplication', 'multiplication')], max_length=30),
        ),
    ]
