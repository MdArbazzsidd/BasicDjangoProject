from django.shortcuts import render
from .forms import TweetForm,SearchForm
from .models import Tweet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-create_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})

def tweet_create(request):
    if request.method == "POST":
        form=TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form= TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method == 'POST':
        form=TweetForm(request.POST , request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})


def tweet_delete(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})


def search_list(request):
    form = SearchForm()
    query = None
    results =[]

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results= Tweet.objects.filter(text__icontains=query).order_by('-create_at')
    return render(request, 'search.html', {'form':form , 'query':query , 'results':results})







