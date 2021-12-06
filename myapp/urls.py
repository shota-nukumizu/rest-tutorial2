from django.urls import path
from . import views

urlpatterns = [
    path('data-list/', views.ListView.as_view()),
    path('data-list/<int:pk>', views.DetailView.as_view()),
]