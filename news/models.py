from django.db import models


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тэг',
        max_length=20,
        unique=True
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=50
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=500
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='',
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(
        verbose_name='Тэги',
        to='Tag'
    )
    views_count = models.PositiveIntegerField(
        verbose_name='Кол-во просмотров',
        default=0
    )
    likes = models.PositiveIntegerField(
        verbose_name='Лайки',
        default=0
    )
    dislikes = models.PositiveIntegerField(
        verbose_name='Дизлайки',
        default=0
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-id',)

    def __str__(self):
        return self.title

