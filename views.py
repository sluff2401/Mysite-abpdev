from django.shortcuts                                 import render
from django.contrib.auth.decorators import login_required

def home_page(request):
  return render(request, 'mysite/home_list.html', {})

def bookmarks_list(request):
  return render(request, 'mysite/bookmarks.html', {})

@login_required
def registrations(request):
  return render(request, 'mysite/registrations.html', {})

@login_required
def local(request):
  return render(request, 'mysite/local.html', {})
