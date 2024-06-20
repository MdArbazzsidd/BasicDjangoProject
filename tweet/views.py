from django.shortcuts import render
from .forms import TweetFrom
from .models import Tweet

from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweet':tweet})

def tweet_create(request):
    if request.method == 'POST':
        form=TweetFrom(request.POST, request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user= request.user
            tweet.save()
        return redirect('tweet_list')
    else:
        form= TweetFrom()
    return render(request, 'tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_edit, user= request.user)
    if request.method == 'POST':
        form=TweetFrom(request.POST , request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetFrom(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})


def tweet_delete(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})