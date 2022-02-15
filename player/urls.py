from django.urls import path
from player import views

urlpatterns = [
    path('', views.PlayerList.as_view()),
    path('<int:pk>/', views.PlayerDetail.as_view())
]