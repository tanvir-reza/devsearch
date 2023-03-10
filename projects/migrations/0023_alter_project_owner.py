# Generated by Django 4.1.4 on 2023-03-03 16:22

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_name_profile_first_name_profile_last_name'),
        ('projects', '0022_alter_project_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(default=users.models.Profile, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
