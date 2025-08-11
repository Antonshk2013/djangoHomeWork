from datetime import datetime

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail

from src.task_manager.models import Task

@receiver(pre_save, sender=Task)
def cache_old_status(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Task.objects.get(pk=instance.pk)
        instance.old_updated_at = old_instance.updated_at
        instance.old_status = old_instance.status
    else:
        instance._old_status = None



@receiver(post_save, sender=Task)
def send_status_changed_email(sender, instance: Task, created: bool, **kwargs):

    if instance.status!=instance.old_status:
        diff = instance.updated_at - instance.old_updated_at
        if diff.total_seconds() >= 5:
            if instance.owner:
                send_mail(
                    subject=f"Change status Task",
                    message=f"Your task '{instance.title}' change status from '{instance.old_status}' to '{instance.status}'",
                    from_email="no-reply@test.com",
                    recipient_list=[instance.owner.email],
                    fail_silently=False,
                )
