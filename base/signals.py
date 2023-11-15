from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db import models

from .models import Room, Notification

@receiver(post_save, sender=Room)
def create_room_notification(sender, instance, created, **kwargs):
    if created:
        # Get all users
        users = get_user_model().objects.all()

        # Create a notification for each user
        for user in users:
            Notification.objects.create(
                recipient=user,
                content=f"{instance.host} has created a new room '{instance.name}', You can join here ."
            )