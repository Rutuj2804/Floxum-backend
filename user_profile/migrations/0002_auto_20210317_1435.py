# Generated by Django 3.1.7 on 2021-03-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='timeline')),
                ('text', models.TextField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('remove', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='timeline',
            field=models.ManyToManyField(to='user_profile.Timeline'),
        ),
    ]
