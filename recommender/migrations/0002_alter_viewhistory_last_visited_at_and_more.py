# Generated by Django 5.0.6 on 2024-05-19 13:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewhistory',
            name='last_visited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='viewhistory',
            name='visited_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='viewhistory',
            unique_together={('user_id', 'product_id')},
        ),
    ]
