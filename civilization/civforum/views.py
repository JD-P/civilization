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

def board(request, board_id=0):
    if request.method == 'GET':
        pboard = PublicBoard.objects.filter(board__id=board_id)[0]
        threads = Thread.objects.filter(board=pboard.board)
        return render(request,
                      'board.html',
                      {'threads':threads})
        
def tracker(request):
    if request.method == 'GET':
        return render(request,
                      'tracker.html',
                      {}) # Placeholder, will add context later
