# Generated by Django 3.1.4 on 2020-12-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.TextField(max_length=50, unique=True),
        ),
    ]
