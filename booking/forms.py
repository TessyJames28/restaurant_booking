# forms.py
from django import forms
from .models import Booking
from datetime import date, datetime

class BookingForm(forms.ModelForm):
    """
    Django form based on booking model that allows
    customers to book a table. Will be integrated in the html template
    """
    class Meta:
        model = Booking
        fields = ['name', 'reservation_date', 'reservation_slot']
        widgets = {
            'reservation_date': forms.DateInput(attrs={
                'type': 'date',
                'id': 'date-picker',
                'min': date.today().isoformat()
            }),
            'reservation_slot': forms.Select(attrs={
                'id': 'slot-select'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control'
            })
        }
        
    def __init__(self, *args, **kwargs):
        """Init method to set reservation date and slot"""
        super().__init__(*args, **kwargs)
        
        # Initially set to empty choices - will be populated via AJAX
        if not self.is_bound:
            self.fields['reservation_slot'].choices = [('', 'Select a date first')]
        
        # Make fields required
        self.fields['name'].required = True
        self.fields['reservation_date'].required = True
        self.fields['reservation_slot'].required = True

    def clean(self):
        """
        Clean method to clean user data and
        prevent duplicate booking/reservations from customsers
        """
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get("reservation_date")
        reservation_slot = cleaned_data.get("reservation_slot")

        if reservation_date and reservation_slot is not None:
            # Check if this slot is already booked
            if Booking.objects.filter(
                reservation_date=reservation_date, 
                reservation_slot=reservation_slot
            ).exists():
                raise forms.ValidationError("This time slot is already booked.")
            
            # Check if the date is not in the past
            if reservation_date < date.today():
                raise forms.ValidationError("Cannot book for past dates.")
            
            # If booking for today, check if time hasn't passed
            if reservation_date == date.today():
                current_hour = datetime.now().hour
                if reservation_slot <= current_hour:
                    raise forms.ValidationError("Cannot book for past time slots.")
        
        return cleaned_data