from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Destinations

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    fun = Destinations.objects.all()
    return render(request,"index.html",{'result':obj,'results':fun})


