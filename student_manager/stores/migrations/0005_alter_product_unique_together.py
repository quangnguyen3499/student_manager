# Generated by Django 3.2.8 on 2022-06-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_cartitem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'brand')},
        ),
    ]
