# Generated by Django 3.0.5 on 2023-08-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
