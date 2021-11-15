from django.shortcuts import render, redirect, reverse
from .models import Play, Review
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect

def movies_list(request):
    article = Play.objects.all().order_by('year')
    return render(request, "articles/movies_list.html", {"articles":article})


def movies_detail(request, slug):
    articles = Play.objects.get(slug=slug)
    all_reviews = Review.objects.all().order_by('movie')
    print(all_reviews)
    isReviewAllowed = check_user_review(request, slug)
    print(isReviewAllowed)
    return render(request, "articles/movies_detail.html", {"articles":articles,'all_reviews': all_reviews, 'isReviewAllowed': isReviewAllowed})



@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        form = forms.CreatePlay(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("movies:home")
    else:
            form = forms.CreatePlay()
    return render(request, "articles/article_create.html", {"form":form})

@login_required(login_url="/accounts/login/")
def sub_review(request, slug):
    form = forms.CreateReview(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        show = Play.objects.get(slug=slug)
        instance.movie = show
        instance.save()
        return redirect("movies:detail", slug=slug)
    else:
        form = forms.CreateReview()
        return render(request, "articles/review.html", {"form":form, "slug":slug})




def check_user_review(request, slug):
    check = Review.objects.values_list('user', 'movie')
    test = Review.objects.count()
    watch = Play.objects.get(slug=slug)
    if test == 0:
        return True
    else:
      for user, movie in check:
          #print(watch.id)
          #print(movie)
          if user == request.user.id and movie == watch.id:
              return False
          else:
              return True




def like_view(request, slug):
    like = Review.objects.get(id=request.POST.get('review_id'))
    like.likes.add(request.user)
    return HttpResponseRedirect(reverse('movies:detail', args=[slug]))








