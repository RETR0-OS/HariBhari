# Generated by Django 4.0.4 on 2022-06-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_alter_blog_likes_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_head',
            field=models.CharField(max_length=40),
        ),
    ]