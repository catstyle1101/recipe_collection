from django.contrib import admin

from foodgram.models import (
    FavoriteRecipe,
    Ingredient,
    Recipe,
    ShoppingCart,
    Tag,
)
from users.models import Subscription, User


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


class UserAdmin(admin.ModelAdmin):
    model = User
    search_fields = ("name", "email")


class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    search_fields = ("user__username", "user__email")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FavoriteRecipe, FavoritesAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(ShoppingCart, CardAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
