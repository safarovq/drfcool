from django.urls import path
from . import views

urlpatterns = [
    path('boys/', views.BoysAPIView.as_view(), name='boys'),
    path('boys/<str:pk>/', views.BoysAPIView.as_view(), name='boys')
]
