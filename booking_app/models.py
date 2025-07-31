from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = [
        ('economy', 'Economy'),
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='rooms', blank=True, null=True)
    capacity = models.PositiveBigIntegerField(default=2)
    type = models.CharField(max_length=20, choices=ROOM_TYPES, default='standard')

    def __str__ (self):
        return f'Room #{self.title}'
    
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
        ordering = ['title', 'price']


class Booking(models.Model):
    STATUSES = [
        ('new', 'New'),
        ('verified', 'Verified'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]

    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUSES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'#{self.room} from {self.check_in} to {self.check_out}'
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural ='Bookings'
        ordering = ['-created_at']