# Generated by Django 3.1.4 on 2020-12-23 09:38

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201222_2202'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique_follow'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, following=django.db.models.expressions.F('user')), name='author_user_not_equal'),
        ),
    ]
