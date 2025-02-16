from django.urls import path
from .views import *

urlpatterns = [
    path('index1/', kurses),
    path('index2/', studentses),
]
