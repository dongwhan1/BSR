from django.shortcuts import render, redirect
from .models import Reservation_Data
from .forms import RESERV_FORM
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
    return render(request, 'reservation/homepage.html')

def schedule(request):
    return render(request, 'reservation/schedule.html')

def makereserv(request):
    if request.method == "POST":
        form = RESERV_FORM(request.POST, request.FILES)
        if form.is_valid():
            reserv = form.save(commit=False)
            reserv.ip = request.META['REMOTE_ADDR']
            reserv.save()
            return redirect('/')
    else:
        form = RESERV_FORM()
    return render(request, 'reservation/makereservation.html', {'form': form})