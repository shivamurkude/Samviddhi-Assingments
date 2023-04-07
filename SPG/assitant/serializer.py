from rest_framework import serializers
from .models import TA


class TAserializer(serializers.ModelSerializer):
    class Meta:
        model=TA
        fields="__all__"