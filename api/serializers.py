from rest_framework import serializers
from Ecommerce.models import Product


# Normal serializers linking to any model defined in the database

class ProductlistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"