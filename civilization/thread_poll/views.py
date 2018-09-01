from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect


def thread_poll(request, board_id=0, poll_id=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return HttpResponse("Testing.")

def new_poll(request, board_id=0):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return HttpResponse("Testing.")
