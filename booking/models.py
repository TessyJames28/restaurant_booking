from django.db import models


# Create your models here.
class Booking(models.Model):
    """
    Model to handle the booking table for customer
    reservations
    """
    # Choices to matcht the time range (10:00-21:00)
    SLOT_CHOICES = [
        (10, '10:00 AM'),
        (11, '11:00 AM'),
        (12, '12:00 PM'),
        (13, '1:00 PM'),
        (14, '2:00 PM'),
        (15, '3:00 PM'),
        (16, '4:00 PM'),
        (17, '5:00 PM'),
        (18, '6:00 PM'),
        (19, '7:00 PM'),
        (20, '8:00 PM'),
        (21, '9:00 PM'),
    ]

    name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(choices=SLOT_CHOICES)

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')

    def __str__(self): 
        return f"{self.name} - {self.reservation_date} at {self.get_reservation_slot_display()}"

    @classmethod
    def get_available_slots(cls, date):
        """Get available slots for a given date"""
        from datetime import datetime
        
        booked_slots = cls.objects.filter(reservation_date=date).values_list('reservation_slot', flat=True)
        all_slots = [choice[0] for choice in cls.SLOT_CHOICES]
        available_slots = [slot for slot in all_slots if slot not in booked_slots]
        
        # If it's today, filter out past hours
        today = datetime.now().date()
        if date == today:
            current_hour = datetime.now().hour
            available_slots = [slot for slot in available_slots if slot > current_hour]
        
        return available_slots


# Add code to create Menu model
class Menu(models.Model):
   """Model to handle menu table"""
   name = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=5, decimal_places=2, null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
   
