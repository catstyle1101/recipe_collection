from django.contrib import admin
from foodgram.models import (
    FavoriteRecipe, Ingredient, Recipe, Tag, ShoppingCart)


class IngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInline,)
    search_fields = ("name", "author__username", "tags__name")
    list_display = ("name", "author", "count_in_favorites")
    list_filter = ("tags__name",)
    raw_id_fields = ("author",)

    def count_in_favorites(self, obj: Recipe) -> int:
        return obj.in_favorites.count()

    count_in_favorites.short_description = "Количество добавлений в избранное"


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_filter = ("name",)


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ("name",)


class FavoritesAdmin(admin.ModelAdmin):
    model = FavoriteRecipe
    list_display = ("user", "recipe")


class CardAdmin(admin.ModelAdmin):
    model = ShoppingCart
    list_display = ("user", "recipe")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(FavoriteRecipe, FavoritesAdmin)
admin.site.register(ShoppingCart, CardAdmin)
