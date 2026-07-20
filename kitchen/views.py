from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from kitchen.forms import CookCreationForm, CookUpdateForm, SearchForm
from kitchen.models import Cook, Dish, DishType



# def index(request):
#     context = {
#         "num_cooks": Cook.objects.count(),
#         "num_dishes": Dish.objects.count(),
#         "num_dish_types": DishType.objects.count(),
#     }
#
#     return render(
#         request,
#         "kitchen/index.html",
#         context=context,
#     )


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_form"] = self.search_form

        return context


class DishTypeListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    search_field = "name"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ("name",)
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ("name",)
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")
    search_field = "name"

class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

class CookListView(LoginRequiredMixin, SearchMixin, generic.ListView):
    model = Cook
    paginate_by = 5
    search_field = "username"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")