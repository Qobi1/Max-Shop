# Generated by Django 4.0.1 on 2022-05-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='price',
            new_name='discount_price',
        ),
        migrations.AddField(
            model_name='category',
            name='real_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
