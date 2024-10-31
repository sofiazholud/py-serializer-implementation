from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2000)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )
