# Generated by Django 4.1.4 on 2023-03-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
