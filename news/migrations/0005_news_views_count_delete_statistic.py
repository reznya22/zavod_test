# Generated by Django 4.2 on 2024-04-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_statistic_news_alter_statistic_views_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
        migrations.DeleteModel(
            name='Statistic',
        ),
    ]