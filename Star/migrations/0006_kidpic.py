# Generated by Django 2.1 on 2019-04-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Star', '0005_validcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='KidPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images')),
                ('star_name', models.CharField(max_length=32)),
            ],
        ),
    ]
