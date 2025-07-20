from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings/', views.bookings_page, name="bookings_page"),
    path('booking_data/', views.bookings, name='booking_data'),
    path('booked_slots/', views.booked_slots, name="booked_slots"),
    path('available-slots/', views.available_slots, name="available_slots"),

]