from rest_framework import serializers

from src.task_manager.models import Category
from src.task_manager.repositories import CategoryRepository

def validate_name(name):
    repository = CategoryRepository()
    category = repository.get_by_name(name)
    if category:
        raise serializers.ValidationError("Category already exists")


class CategoryCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        validators=[
            validate_name
        ]
    )
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        try:
            repository = CategoryRepository()
            category = repository.create(validated_data)
            return category
        except Exception as e:
            raise serializers.ValidationError(str(e))

    def update(self, instance, validated_data):
        try:
            repository = CategoryRepository()
            update_category = repository.update(instance, **validated_data)
            return update_category
        except Exception as e:
            raise serializers.ValidationError(str(e))
