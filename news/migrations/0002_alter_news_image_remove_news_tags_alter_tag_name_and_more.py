# Generated by Django 4.2 on 2024-04-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='Картинка'),
        ),
        migrations.RemoveField(
            model_name='news',
            name='tags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Тэг'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.tag', verbose_name='Тэги'),
        ),
    ]