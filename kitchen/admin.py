from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import Cook, Dish, DishType


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional information",
            {
                "fields": (
                    "years_of_experience",
                ),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "years_of_experience",
                ),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "years_of_experience",
        "is_staff",
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "dish_type",
        "price",
    )
    list_filter = ("dish_type",)
    search_fields = ("name",)
    filter_horizontal = ("cooks",)
