from django.urls import path
from .views import MainView, TestView, TourView, DepartureView


urlpatterns = [
    path('', MainView.as_view(), name="index"),
    path('tour/<int:id>/', TourView.as_view(), name="tour"),
    path('departure/<str:departure>/', DepartureView.as_view(), name="departure"),
]
