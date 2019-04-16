from django.shortcuts import render
from .models import Tank
from django.db import models
from django.http import HttpResponse
from django.views import View


# Create your views here.

# The view for the created model Tank
def tank_view(request):
    queryset = Tank.objects.all()
    context = {
        'object': queryset
    }
    return render(request, "tankbattle.html", context)


def tank_1(request, pk):
    queryset = Tank.objects.get(pk=1)
    context = {
        'object': queryset
    }
    return render(request, 'tankbattle.html', context)


def tank_2(request, pk):
    queryset = Tank.objects.get(pk=2)
    context = {
        'object': queryset
    }
    return render(request, 'tankbattle.html', context)


def tank_3(request, pk):
    queryset = Tank.objects.get(pk=3)
    context = {
        'object': queryset
    }
    return render(request, 'tankbattle.html', context)


def tank_4(request, pk):
    queryset = Tank.objects.get(pk=4)
    context = {
        'object': queryset
    }
    return render(request, 'tankbattle.html', context)
