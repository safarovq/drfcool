from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'boys', views.BoysViewSet)

urlpatterns = [
    # path('boys/', views.BoysViewSet.as_view({'get': 'list'}), name='boys'),
    # # path('boys/<str:pk>/', views.BoysViewSet.as_view(), name='boys'),
    # # path('boys/crud/<str:pk>/', views.BoysViewSet.as_view({'put': 'update',
    #                                                        'post': 'create'}),
    #      name='boys')

    path('', include(router.urls)),
]
