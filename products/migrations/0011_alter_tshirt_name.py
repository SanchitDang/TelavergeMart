# Generated by Django 5.0.6 on 2024-05-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_brand_title_alter_color_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
