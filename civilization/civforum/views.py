from django.shortcuts import render
from django.http.response import HttpResponse
from civforum.models import *

# Create your views here.

def boards(request):
    if request.method == 'GET':
        return render(request,
                      'boards.html',
                      {'public_boards':PublicBoard.objects.all()})
    else:
        HttpResponse("POST requests not accepted on this view.")

def tracker(request):
    if request.method == 'GET':
        return render(request,
                      'tracker.html',
                      {}) # Placeholder, will add context later
