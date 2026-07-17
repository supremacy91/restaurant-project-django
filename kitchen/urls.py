from django.urls import path

from kitchen.views import index, DishListView, DishTypeListView

app_name = "kitchen"

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
]
