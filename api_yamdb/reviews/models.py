from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from library.models import Title

CustomUser = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    text = models.TextField("Текст", help_text="Отзывы")
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор",
    )
    score = models.PositiveSmallIntegerField(
        verbose_name="Оценка",
        validators=(
            MinValueValidator(
                1,
                message='Введённая оценка не валидна'
            ),
            MaxValueValidator(
                10,
                message='Введённая оценка не валидна'
            ),
        ),
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True,
                                    db_index=True)

    class Meta:
        ordering = ("-pub_date", )
        constraints = [
            models.UniqueConstraint(
                fields=["author", "title"], name="unique_review"
            )
        ]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField("Текст", help_text="Комментарий")
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments"
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        ordering = ("-pub_date", )

    def __str__(self):
        return self.text[:15]
