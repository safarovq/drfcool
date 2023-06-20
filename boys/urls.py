from django.urls import path
from . import views

urlpatterns = [
    path('boys/', views.BoysAPIView.as_view(), name='boys')
]
