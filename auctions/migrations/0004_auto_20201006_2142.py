# Generated by Django 3.1.1 on 2020-10-07 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201005_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='listed_by',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
