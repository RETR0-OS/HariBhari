# Generated by Django 4.0.4 on 2022-05-11 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_remove_blog_blog_image_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
