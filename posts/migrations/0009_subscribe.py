# Generated by Django 3.2.13 on 2022-04-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_comment_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]