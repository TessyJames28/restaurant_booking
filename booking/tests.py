from django.test import TestCase, Client
from django.urls import reverse
from .models import Booking, Menu
from datetime import date

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        # Create sample menu item
        self.menu_item = Menu.objects.create(
            name="Greek Salad",
            price=8.00,
            menu_item_description="Fresh Greek salad"
        )
        # Create sample booking
        self.booking = Booking.objects.create(
            name="John Doe",
            reservation_date=date.today(),
            reservation_slot=1
        )

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")

    def test_book_view_get(self):
        response = self.client.get(reverse("book"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "book.html")

    def test_bookings_api(self):
        response = self.client.get(reverse("booking_data"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))
        self.assertIn("name", response.json()[0])

    def test_available_slots_valid(self):
        response = self.client.get(reverse("available_slots"), {"date": str(date.today())})
        self.assertEqual(response.status_code, 200)
        self.assertIn("available_slots", response.json())

    def test_available_slots_no_date(self):
        response = self.client.get(reverse("available_slots"))
        self.assertEqual(response.status_code, 400)

    def test_booked_slots_valid(self):
        response = self.client.get(reverse("booked_slots"), {"date": str(date.today())})
        self.assertEqual(response.status_code, 200)
        self.assertIn("booked_slots", response.json())

    def test_menu_view(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu.html")

    def test_display_menu_item_view(self):
        response = self.client.get(reverse("menu_item", args=[self.menu_item.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu_item.html")
