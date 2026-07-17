from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

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


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 5


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = ("name",)
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = ("name",)
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5