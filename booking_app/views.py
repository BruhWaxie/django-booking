from django.shortcuts import render
from booking_app.models import Room, Booking
# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', context={'rooms':rooms})