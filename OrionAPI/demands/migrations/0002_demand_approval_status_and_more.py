# Generated by Django 4.1.7 on 2023-03-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='approval_status',
            field=models.CharField(choices=[('APPROVED', 1), ('DENIED', 2), ('WAITING', 3)], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='demand',
            name='approver_approval_status',
            field=models.CharField(choices=[('APPROVED', 1), ('DENIED', 2), ('WAITING', 3)], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='demand',
            name='note',
            field=models.TextField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='demand',
            name='receiver_approval_status',
            field=models.CharField(choices=[('APPROVED', 1), ('DENIED', 2), ('WAITING', 3)], max_length=100, null=True),
        ),
    ]