# Generated by Django 3.2.13 on 2022-04-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220419_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, 'FASHION'), (1, 'TRAVEL')], null=True),
        ),
    ]