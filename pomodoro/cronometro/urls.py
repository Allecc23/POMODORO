from django.urls import path, include
from rest_framework import routers
from viewsets import UsuarioViewSet
from .views import home, pomodoro, dashboard, historico, createUsuario,readUsuario, updateUsuario, deleteUsuario
urlpatterns = [
    path('', home, name='home'),
    path('app/', pomodoro, name='pomodoro'),
    path('dashboard/',dashboard, name='dashboard'),
    path('historico/', historico, name='historico'),
]

router = routers .DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename="usuario")

urlpatterns =[

    path('createUsuario', createUsuario, name='createUsuario'),
    path('readUsuario', readUsuario, name='readUsuario'),
    path('updateUsuario/<int:id>', updateUsuario, name='updateUsuario'),
    path('deleteUsuario', deleteUsuario, name='deleteUsuario'),
    path('api/', include(router.urls)),
]

