# Generated by Django 2.0.4 on 2018-05-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='create_time',
        ),
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='article',
            name='popular_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='views_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='weight',
            field=models.CharField(default=0, max_length=64),
        ),
    ]
