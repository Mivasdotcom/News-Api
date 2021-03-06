# Generated by Django 3.1.7 on 2021-03-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NewsStories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=64)),
                ('category', models.CharField(choices=[('pol', 'politics'), ('art', 'art'), ('tech', 'technology'), ('trivia', 'triva news')], default='unknown', max_length=32)),
                ('region', models.CharField(choices=[('uk', 'uk'), ('eu', 'european news'), ('w', 'world news')], default='unknown', max_length=10)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=512)),
            ],
        ),
    ]
