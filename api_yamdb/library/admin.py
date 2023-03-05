from django.contrib import admin
from library.models import Category, Genre, Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'year', 'description', 'category',)
    search_fields = ('name',)
    list_filter = ('year',)
    list_editable = ('category',)
    list_display_links = ('name',)
    empty_value_display = '-пусто-'

    def __str__(self):
        return self.name[:15]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('name',)
