# Generated by Django 3.1.7 on 2021-03-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210317_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postimages',
            name='image',
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_five',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_four',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_one',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_seven',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_six',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_three',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
        migrations.AddField(
            model_name='postimages',
            name='image_two',
            field=models.FileField(null=True, upload_to='', verbose_name='posts'),
        ),
    ]
