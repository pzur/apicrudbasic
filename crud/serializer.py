from rest_framework import serializers, viewsets
from .models import Post

class PostSerializer (serializers.ModelSerializer): 
  class Meta: 
    model = Post 
    fields = ('id', 'title', 'message')       