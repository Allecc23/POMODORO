from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

def home(request):
    return render(request, 'home.html')
def pomodoro(request):
    return render(request, 'pomodoro.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def historico(request):
    return render(request, 'historico.html')
# Create your views here.

def home (request):
    return render (request, 'home.html')

def createUsuario(request):
    usuarioForm = UsuarioForm(request.Post or None)
    if(usuarioForm.is_valid()):
        usuario = usuarioForm.save(commit= false)
        usuario.save()
        return redirect("readusuario")
    return render(request, 'createusuario.html', {'usuarioForm': usuarioForm})

def readUsuario(request):
    usuario = Usuario.objects.all()
    return render(request, 'readusuario.html', {'usuario': usuario})


def updateUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuarioForm = UsuarioForm(request.Post or None, instance=usuario)
    if(usuarioForm.is_valid()):
        usuario = usuarioForm.save(commit= false)
        usuario.save()
        return redirect("readusuario")
    return render(request, 'createusuario.html', {'usuarioForm': usuarioForm})

def deleteUsuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()
    return redirect("readusuario")