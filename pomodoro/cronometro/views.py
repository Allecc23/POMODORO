from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def pomodoro(request):
    return render(request, 'pomodoro.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def historico(request):
    return render(request, 'historico.html')
# Create your views here.
