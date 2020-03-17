from .models import Product , Review
from rest_framework import serializers


class ProductApi(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewApi(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'