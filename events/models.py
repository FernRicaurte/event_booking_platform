from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    """
Represents an event in the event booking platform.

Args:
    title (str): The title of the event.
    description (str): The description of the event.
    date (datetime.date): The date of the event.
    time (datetime.time): The time of the event.
    location (str): The location of the event.
    organizer (User): The user who organized the event.

Attributes:
    title (str): The title of the event.
    description (str): The description of the event.
    date (datetime.date): The date of the event.
    time (datetime.time): The time of the event.
    location (str): The location of the event.
    organizer (User): The user who organized the event.
    created_at (datetime.datetime): The timestamp when the event was created.
"""
    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)  
    """
Represents a registration for an event in the event booking platform.

Args:
    event (Event): The event being registered for.
    attendee (User): The user who is attending the event.

Attributes:
    event (Event): The event being registered for.
    attendee (User): The user who is attending the event.
    registration_date (datetime.datetime): The timestamp when the registration was created.

Returns:
    str: A string representation of the registration, 
    showing the username of the attendee and the title of the event.
"""
def __str__(self):
    return f"{self.attendee.username} - {self.event.title}"
