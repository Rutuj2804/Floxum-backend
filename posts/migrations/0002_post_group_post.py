# Generated by Django 3.1.7 on 2021-03-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group_post',
            field=models.BooleanField(default=False),
        ),
    ]
