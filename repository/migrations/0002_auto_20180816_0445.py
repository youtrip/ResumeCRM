# Generated by Django 2.0.7 on 2018-08-16 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumesubscription',
            name='trigger_time',
            field=models.DateTimeField(auto_now=True, verbose_name='收藏时间'),
        ),
    ]