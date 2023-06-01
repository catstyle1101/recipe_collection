from django.contrib import admin


from users.models import User
from foodgram.models import Recipe, Tag


class RecipeAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)