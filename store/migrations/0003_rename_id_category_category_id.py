# Generated by Django 4.0.5 on 2022-06-05 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='id',
            new_name='category_id',
        ),
    ]
