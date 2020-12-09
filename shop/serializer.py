from rest_framework import serializers
from .models import Business


class BizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields=('name','location','photo','contactInfo','price_range','hours','category','other_details'       )
