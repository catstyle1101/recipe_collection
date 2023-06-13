from django.contrib import admin

from users.models import User, Subscription


class UserAdmin(admin.ModelAdmin):
    model = User
    search_fields = ("name", "email")

class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    search_fields = ("user__username", "user__email")

admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
