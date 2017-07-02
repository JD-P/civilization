from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from civforum.models import *
from django.db.models import Max, F, QuerySet
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
                      {'pboard':pboard,
                       'threads':threads})

def thread(request, board_id, thread_id, page_number=0):
    """Individual thread view. Threads only have ten posts a page and end 
    after ten pages of discussion."""
    if request.method == 'POST':
        HttpResponse("You use the newpost view to add messages to a thread.")
    elif request.method == 'GET':
        if request.user.is_authenticated():
            thread = Thread.objects.filter(id=thread_id)[0]
            tbody_max = TBody.objects.aggregate(Max('version'))['version__max']
            tbody = TBody.objects.filter(version=tbody_max)[0]
            tposts = TPost.objects.filter(thread=thread)
            return render(request,
                          'thread.html',
                          {'thread':thread,
                           'tbody':tbody,
                           'tposts':tposts})
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        HttpResponse("Nothing weird now, just use a GET request.")
    
    
def newthread(request, board_id=0):
    if request.user.is_authenticated():
            user_id = request.user.id
    else:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
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
            for tag in form.cleaned_data["tags"].lower().split(","):
                if not Tag.objects.filter(string=tag):
                    tag = Tag(string=tag)
                    tag.save()
                else:
                    tag = Tag.objects.filter(string=tag)[0]
                ttag = TTag(thread=thread,
                            tag=tag,
                            tagger=user,
                            creation_date=now)
                ttag.save()
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

def newpost(request, board_id=0, thread_id=0):
    if request.user.is_authenticated():
        user_id = request.user.id
    else:
        HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
        thread = Thread.objects.filter(id=thread_id)[0]
        now = datetime.utcfromtimestamp(time())
        form = forms.NewPostForm(request.POST)
        clean = form.is_valid()
        mood = Mood.objects.filter(id=form.cleaned_data["mood"])[0]
        if clean:
            post = TPost(thread=thread,
                        author=request.user,
                        creation_date=now,
                        body=form.cleaned_data["body"],
                        mood=mood)
            post.save()
            return HttpResponseRedirect(reverse('thread',
                                                kwargs={'board_id':board_id,
                                                        'thread_id':thread_id,
                                                        'page_number':0}))
    elif request.method == 'GET':
        form = forms.NewPostForm()
    return render(request,
                  'newpost.html',
                  {'board_id':board_id,
                   'thread_id':thread_id,
                   'form':form})

def tracker(request):
    if request.method == 'GET':
        return render(request,
                      'tracker.html',
                      {}) #TODO: Placeholder, will add context later

def search(request):
    if request.method == 'GET':
        if request.GET.get("searchbar",False):
            search = request.GET.get("searchbar")
            result_sets = []
            author_results = Thread.objects.filter(author__username__icontains=search)
            if author_results:
                result_sets.append(author_results)
            thread_results = Thread.objects.filter(tbody__body__icontains=search)
            if thread_results:
                result_sets.append(thread_results)
            results = QuerySet.union(*result_sets)
            print(results[0])
            return render(request,
                          'search_results.html',
                          {'results':results})
        form = forms.SimpleSearchForm()
        return render(request,
                      'search.html',
                      {'form':form})
