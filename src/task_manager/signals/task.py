from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from src.task_manager.models import Task


@receiver(post_save, sender=Task)
def category_saved(sender, instance: Task, created: bool, **kwargs):
    print("=" * 100)
    print("=" * 100)

    print(f"Our sender is {sender}")
    if created:
        send_mail(
            subject='Тема письма',
            message='Текст письма',
            from_email="admin@test_domain.com",
            recipient_list=['receiver@example.com'],
            fail_silently=False,
        )
        print(f"New category was created: '{instance.title}'")
    else:
        print(f"Category '{instance.title}' was updated")

    print("=" * 100)
    print("=" * 100)