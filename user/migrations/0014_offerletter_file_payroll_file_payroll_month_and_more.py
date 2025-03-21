# Generated by Django 5.1.1 on 2024-10-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerletter',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='offer_letters/'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='payrolls/'),
        ),
        migrations.AddField(
            model_name='payroll',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='payroll',
            unique_together={('employee', 'month')},
        ),
    ]
