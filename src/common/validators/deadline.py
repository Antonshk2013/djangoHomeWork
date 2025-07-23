from django.utils import timezone
from rest_framework import serializers

def validate_deadline_field(deadline: timezone):
    now = timezone.now()
    if deadline < now:
        raise serializers.ValidationError("Deadline must be now or in the future")