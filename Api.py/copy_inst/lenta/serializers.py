from rest_framework import serializers
from .models import Post, AAA, Book


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AAASerializer(serializers.ModelSerializer):
    class Meta:
        model = AAA
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'