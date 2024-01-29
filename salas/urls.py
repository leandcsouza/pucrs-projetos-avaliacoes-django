from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar/', views.SalaView.as_view(), name='salas'),
]
