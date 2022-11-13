from rest_framework.serializers import ModelSerializer
from .models import Index


class IndexSerializer(ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'name', 'number']
