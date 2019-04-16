from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View for the home page


def index_view(request, *args, **kwargs):
    return render(request, "index.html")
