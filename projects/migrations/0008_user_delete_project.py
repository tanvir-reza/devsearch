# Generated by Django 4.1.4 on 2023-01-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
