from django.urls import path

from .views import (
    PoliticiansListAPIView,
    PoliticianDetailAPIView,
    PoliticianCreateAPIView,
    PoliticianUpdateAPIView,
    PoliticianDeleteAPIView,
)


urlpatterns = [
    path('list/<int:pk>',PoliticianDetailAPIView.as_view()),
    path('list',PoliticiansListAPIView.as_view()),
    path('new',PoliticianCreateAPIView.as_view()),
    path('update/<int:pk>',PoliticianUpdateAPIView.as_view()),
    path('delete/<int:pk>',PoliticianDeleteAPIView.as_view()),
]