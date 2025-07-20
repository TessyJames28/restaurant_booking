# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Menu
from .models import Booking
from datetime import datetime
from django.contrib import messages
from .forms import BookingForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


def home(request):
    """
    Displays the index page
    endpoint: "http://127.0.0.1:8000/"
    """
    return render(request, 'index.html')

def about(request):
    """
    Displays the about page
    endpoint: "http://127.0.0.1:8000/about/"
    """
    return render(request, 'about.html')


def book(request):
    """
    Displays the book page
    endpoint: "http://127.0.0.1:8000/book/"
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            # Display a sucess message upon successful booking
            messages.success(request, f"Your table has been booked successfully for {booking.get_reservation_slot_display()} on {booking.reservation_date}!")
            return redirect("book")
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = BookingForm()
    
    context = {'form': form}
    return render(request, 'book.html', context)


def bookings_page(request):
    """
    Returns the html page that displays all booking
    This serves as a dashboard for admins
    endpoint: "http://127.0.0.1:8000/bookings/"
    """
    return render(request, 'bookings.html')

def bookings(request):
    """
    Return all bookings as JSON
    Works with bookings_page to display data on html page
    """
    bookings = Booking.objects.all().values(
        'id', 'name', 'reservation_date', 'reservation_slot'
    ).order_by('reservation_date', 'reservation_slot')
    
    # Convert to more readable format
    booking_list = []
    for booking in bookings:
        # Get the display name for the slot
        slot_display = dict(Booking.SLOT_CHOICES).get(booking['reservation_slot'], 'Unknown')
        booking_list.append({
            'id': booking['id'],
            'name': booking['name'],
            'date': booking['reservation_date'].strftime('%Y-%m-%d'),
            'time': slot_display
        })
    
    return JsonResponse(booking_list, safe=False)

@require_http_methods(["GET"])
def available_slots(request):
    """
    Return available slots for a given date
    """
    date_str = request.GET.get('date')
    
    if not date_str:
        return JsonResponse({'error': 'No date provided'}, status=400)
    
    try:
        # Parse the date
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Get available slots using the model method
        available_slot_numbers = Booking.get_available_slots(selected_date)
        
        # Convert to the format expected by the frontend
        available_slots = []
        for slot_number in available_slot_numbers:
            slot_display = dict(Booking.SLOT_CHOICES).get(slot_number, f'{slot_number}:00')
            available_slots.append({
                'value': slot_number,
                'display': slot_display
            })
        
        return JsonResponse({
            'available_slots': available_slots,
            'date': date_str
        })
    
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def booked_slots(request):
    """
    Return booked slots for a given date (legacy endpoint)
    """
    date_str = request.GET.get('date')
    
    if not date_str:
        return JsonResponse({'error': 'No date provided'}, status=400)
    
    try:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        booked = Booking.objects.filter(reservation_date=selected_date).values_list('reservation_slot', flat=True)
        return JsonResponse({'booked_slots': list(booked)})
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def menu(request):
    """
    Displays the menu page
    endpoint: "http://127.0.0.1:8000/menu/"
    """
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    """
    function to display menu items for users to view
    """
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 