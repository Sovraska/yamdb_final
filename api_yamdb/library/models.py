from django.db import models


class Category(models.Model):

    name = models.CharField('Название', max_length=256)
    slug = models.SlugField(
        'Слаг',
        unique=True,
        max_length=50,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):

    name = models.CharField('Название', max_length=256)
    slug = models.SlugField(
        'Слаг',
        unique=True,
        max_length=50,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name[:15]


class Title(models.Model):

    name = models.CharField('Название', max_length=256)
    year = models.IntegerField()
    description = models.TextField('Описание')

    genre = models.ManyToManyField(
        Genre,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
        related_name='titles',
        verbose_name='Категория',
        on_delete=models.SET_NULL, null=True,
        help_text='Выберите категорию',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name[:15]
