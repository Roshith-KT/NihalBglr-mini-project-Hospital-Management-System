# Generated by Django 3.0.5 on 2023-08-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_patient_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='prescription',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
