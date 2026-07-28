from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import (
    CookCreationForm,
    CookUpdateForm,
    DishForm,
    SearchForm,
)
from kitchen.models import Cook, Dish, DishType


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "kitchen/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dish_statistics = Dish.objects.aggregate(
            average_price=Avg("price"),
        )

        context["num_dishes"] = Dish.objects.count()
        context["num_cooks"] = Cook.objects.count()
        context["num_dish_types"] = DishType.objects.count()
        context["average_price"] = dish_statistics["average_price"]

        context["dish_types"] = DishType.objects.annotate(
            dish_count=Count("dishes"),
        ).order_by("name")

        context["recent_dishes"] = (
            Dish.objects.select_related("dish_type")
            .order_by("-pk")[:5]
        )

        return context


class SearchMixin:
    search_field = None

    def get_queryset(self):
        queryset = super().get_queryset()

        self.search_form = SearchForm(self.request.GET)

        if self.search_form.is_valid():
            query = self.search_form.cleaned_data["query"]

            if query:
                queryset = queryset.filter(
                    **{f"{self.search_field}__icontains": query}
                )

        return queryset


class DishTypeListView(
    LoginRequiredMixin,
    SearchMixin,
    generic.ListView,
):
    model = DishType
    paginate_by = 5
    search_field = "name"

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.annotate(
            dish_count=Count("dishes"),
        )


class DishTypeCreateView(
    LoginRequiredMixin,
    generic.CreateView,
):
    model = DishType
    fields = ("name",)
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(
    LoginRequiredMixin,
    generic.UpdateView,
):
    model = DishType
    fields = ("name",)
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(
    LoginRequiredMixin,
    SearchMixin,
    generic.ListView,
):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")
    search_field = "name"

    def get_queryset(self):
        queryset = super().get_queryset()

        dish_type_id = self.request.GET.get("type")

        if dish_type_id:
            queryset = queryset.filter(dish_type_id=dish_type_id)

        return queryset


class DishDetailView(
    LoginRequiredMixin,
    generic.DetailView,
):
    model = Dish


class DishCreateView(
    LoginRequiredMixin,
    generic.CreateView,
):
    model = Dish
    form_class = DishForm


class DishUpdateView(
    LoginRequiredMixin,
    generic.UpdateView,
):
    model = Dish
    form_class = DishForm


class DishDeleteView(
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(
    LoginRequiredMixin,
    SearchMixin,
    generic.ListView,
):
    model = Cook
    paginate_by = 5
    search_field = "username"


class CookDetailView(
    LoginRequiredMixin,
    generic.DetailView,
):
    model = Cook


class CookCreateView(
    LoginRequiredMixin,
    generic.CreateView,
):
    model = Cook
    form_class = CookCreationForm


class CookUpdateView(
    LoginRequiredMixin,
    generic.UpdateView,
):
    model = Cook
    form_class = CookUpdateForm


class CookDeleteView(
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")