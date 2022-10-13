from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bookings.html')

def home(request):
    return render(request,'food.html')

def rom(request):
    return render(request,'room.html')

def roh(request):
    return render (request,'pool.html')
