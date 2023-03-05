from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role'
    )
    search_fields = ('username',)
    list_editable = ('role',)
    list_display_links = ('username',)
    empty_value_display = '-пусто-'

    def __str__(self):
        return self.username[:15]
