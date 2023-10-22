from django.shortcuts import render

from demokapp.models import place


# Create your views here.
def desk(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})