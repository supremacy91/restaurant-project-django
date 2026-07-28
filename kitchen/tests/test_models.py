from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook, Dish, DishType


class DishTypeModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Main Course")

        self.assertEqual(
            str(dish_type),
            "Main Course",
        )


class CookModelTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="john_smith",
            password="TestPassword123!",
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            years_of_experience=5,
        )

    def test_cook_str(self):
        self.assertEqual(
            str(self.cook),
            "john_smith",
        )

    def test_cook_get_absolute_url(self):
        expected_url = reverse(
            "kitchen:cook-detail",
            kwargs={"pk": self.cook.pk},
        )

        self.assertEqual(
            self.cook.get_absolute_url(),
            expected_url,
        )

    def test_cook_default_years_of_experience(self):
        cook = Cook.objects.create_user(
            username="emma_wilson",
            password="TestPassword123!",
        )

        self.assertEqual(
            cook.years_of_experience,
            0,
        )


class DishModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="Dessert",
        )

        self.dish = Dish.objects.create(
            name="Chocolate Cake",
            description="Chocolate cake with cream",
            price="12.50",
            dish_type=self.dish_type,
        )

    def test_dish_str(self):
        self.assertEqual(
            str(self.dish),
            "Chocolate Cake",
        )

    def test_dish_type_relationship(self):
        self.assertEqual(
            self.dish.dish_type,
            self.dish_type,
        )

    def test_dish_can_have_multiple_cooks(self):
        first_cook = Cook.objects.create_user(
            username="marco",
            password="TestPassword123!",
        )

        second_cook = Cook.objects.create_user(
            username="sophie",
            password="TestPassword123!",
        )

        self.dish.cooks.set(
            [
                first_cook,
                second_cook,
            ]
        )

        self.assertEqual(
            self.dish.cooks.count(),
            2,
        )

        self.assertIn(
            first_cook,
            self.dish.cooks.all(),
        )

        self.assertIn(
            second_cook,
            self.dish.cooks.all(),
        )