from django.shortcuts import render
from rest_framework import viewsets, status
from .serializer import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post

#Recordar que ModelViewSet permite que se realice todas las operaciones del CRUD
#tales como Create (POST) READ (GET) UPDATE(PUT) DELETE (DELETE)

class PostView(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer



    

