# Generated by Django 3.1.7 on 2021-03-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_timeline_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='user'),
        ),
    ]
