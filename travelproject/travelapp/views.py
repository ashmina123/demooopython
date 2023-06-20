from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

#create your views here.
def demo(request):
  obj=Place.objects.all()
  return render(request,"index.html",{'result':obj})