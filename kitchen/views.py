from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType


def index(request):
    context = {
        "num_cooks": Cook.objects.count(),
        "num_dishes": Dish.objects.count(),
        "num_dish_types": DishType.objects.count(),
    }

    return render(
        request,
        "kitchen/index.html",
        context=context,
    )
