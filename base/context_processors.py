'''from .models import Notification

def user_notification(request):
    context = {}

    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            user = request.user
        ).order_by(-created_date)
        unseen = notifications.exclude(is_seen=True)
        context['notifications'] = notifications
        context['unseen'] = unseen.count()
    return context'''