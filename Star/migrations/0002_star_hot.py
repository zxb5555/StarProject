# Generated by Django 2.1 on 2019-04-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='hot',
            field=models.CharField(default='false', max_length=32),
            preserve_default=False,
        ),
    ]