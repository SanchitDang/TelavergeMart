# Generated by Django 3.0.8 on 2020-11-27 20:01

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_order_order_item_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='ideal_for',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='neck_type',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='occassion',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='sleeve_type',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='title', unique=True),
        ),
    ]
