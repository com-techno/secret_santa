from django.contrib import admin


from .models import Game, Gamer, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')



admin.site.register(User)
admin.site.register(Gamer)
admin.site.register(Game)

