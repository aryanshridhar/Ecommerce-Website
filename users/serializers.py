from rest_framework import serializers
from .models import Profile

class ProfileApi(serializers.Serializer):
    class Meta:
        model = Profile
        fields = '__all__'