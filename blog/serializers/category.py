from rest_framework import serializers
from ..models import  Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')