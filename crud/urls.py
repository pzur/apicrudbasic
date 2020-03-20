from django.urls import path, include
from .views import PostView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('crear',PostView)

urlpatterns = [
    path('',include(router.urls)),  
]



