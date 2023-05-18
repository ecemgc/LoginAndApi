# Generated by Django 4.1.7 on 2023-03-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='status_changed',
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('PASSIVE', 'passive')], default='active', max_length=15),
        ),
    ]