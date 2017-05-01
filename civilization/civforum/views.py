from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from civforum.models import *
from django.contrib.auth.models import User
from civforum import forms
from time import time
from datetime import datetime

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

def newthread(request, board_id=0):
    if request.method == 'POST':
        if request.user.is_authenticated():
            user_id = request.user.id
        else:
            return HttpResponse("You're not logged in. :P")
        now = datetime.utcfromtimestamp(time())
        form = forms.NewThreadForm(request.POST)
        clean = form.is_valid()
        pboard = PublicBoard.objects.filter(board__id=form.cleaned_data["board_id"])[0]
        purpose = Purpose.objects.filter(id=form.cleaned_data["purpose_id"])[0]
        rigor = Rigor.objects.filter(id=form.cleaned_data["rigor_id"])[0]
        user = User.objects.filter(id=user_id)[0]
        if pboard and clean:
            thread = Thread(board=pboard.board,
                            title=form.cleaned_data["title"],
                            author=user,
                            rigor=rigor,
                            posts=1,
                            creation_date=now,
                            last_activity=now)
            thread.save()
            tbody = TBody(thread=thread,
                          version=now,
                          body=form.cleaned_data["tbody"])
            purpose = TPurpose(thread=thread,
                               purpose=purpose)
            #TODO: Tags not implemented right now
            tbody.save()
            purpose.save()
            return HttpResponseRedirect(
                reverse('board',
                        kwargs={
                            'board_id':form.cleaned_data["board_id"]}))
    elif request.method == 'GET':
        initial = {'board_id':board_id}
        form = forms.NewThreadForm(initial)

    return render(request,
                  'newthread.html',
                  {'board_id':board_id,
                   'form':form})

def tracker(request):
    if request.method == 'GET':
        return render(request,
                      'tracker.html',
                      {}) #TODO: Placeholder, will add context later
