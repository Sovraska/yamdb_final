from django.contrib import admin

from reviews.models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date',)
    search_fields = ('title',)
    list_display_links = ('title',)
    empty_value_display = '-пусто-'

    def __str__(self):
        return self.title[:15]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review_id', 'text', 'author', 'pub_date',)
    search_fields = ('text',)
    list_display_links = ('review_id',)
    empty_value_display = '-пусто-'

    def __str__(self):
        return self.text[:15]
