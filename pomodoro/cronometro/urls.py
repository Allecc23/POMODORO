from django.urls import path
from .views import home, pomodoro, dashboard, historico
urlpatterns = [
    path('', home, name='home'),
    path('app/', pomodoro, name='pomodoro'),
    path('dashboard/',dashboard, name='dashboard'),
    path('historico/', historico, name='historico'),
]