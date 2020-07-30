# Generated by Django 3.0.7 on 2020-07-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('MyBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotationchart',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='是否是active'),
        ),
        migrations.AlterField(
            model_name='rotationchart',
            name='title',
            field=models.CharField(max_length=70, verbose_name='轮播图标题'),
        ),
    ]
