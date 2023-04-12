from django.shortcuts import render, redirect
from . import models
from django.http import JsonResponse
from django.db.models import Max
from django.db.models import Min
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    alumnos = models.Alumno.objects.all
    califs = models.CalifLog.objects.all
    numAlumni = models.Alumno.objects.count()
    maxp = models.CalifLog.objects.all().aggregate(Max('calificacion'))
    minp = models.CalifLog.objects.all().aggregate(Min('calificacion'))
    avg = models.CalifLog.objects.aggregate(Avg('calificacion'))
    ctx = {'alumnos': alumnos, 'califs': califs, 
           'numAlumni':numAlumni, 'avgcalif':avg,
           'maxp': maxp, 'minp': minp}
    return render(request, "frontend/index.html", ctx)


def chart(request):
    maxp = models.CalifLog.objects.all().aggregate(Max('calificacion'))
    pointlist = models.CalifLog.objects.all().order_by('timestamp')
    ctx = {'maxp':maxp["calificacion__max"], "pointlist": pointlist}
    return render(request, "frontend/chart.html",ctx)


def about_us(request):
    return render(request, "frontend/aboutus.html")


def log(request):
    # Data
    lastestlogs = list(models.CalifLog.objects.all().order_by('timestamp')[:10].values())
    # JsonResponse
    return JsonResponse(lastestlogs, safe=False)


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            messages.error(request, ("Usuario o contraseña incorrecta."))
            return redirect('login')

    return render(request, 'frontend/login.html')


def logoutview(request):
    logout(request)
    messages.success(request, ("Logout Exitoso"))
    return redirect('login')