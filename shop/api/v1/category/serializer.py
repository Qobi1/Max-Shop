from rest_framework import serializers

from shop_app.models import *


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



