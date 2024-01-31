from django.http import HttpResponse
from django.shortcuts import render

from .models import filt

# Create your views here.
def filter(request):
    fil = filt.objects.all()
    contex = {"fil": fil}
    return render(request, "filters.html", contex)