# Generated by Django 4.1.4 on 2023-01-08 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('demo_link', models.URLField()),
                ('vote_ration', models.DecimalField(decimal_places=1, max_digits=2)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
