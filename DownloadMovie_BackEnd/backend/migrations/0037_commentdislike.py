# Generated by Django 4.0.6 on 2022-09-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0036_commentlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
