from django.shortcuts import render
from django.http import HttpResponse
# from session_app.models import Album
# Create your views here.

def home(request):
    a  = Album.objects.all()
    return render(request,"dhun/home.html",{"Album":a})

def index(request):
    num_author = Author.objects.count()
    request.session.set_test_cookie()
    num_visit = request.session.get('numvisit',0)
    request.session['num_visit'] = num_visit + 1
    context = {
        'num_book':num_books,
        'num_instances':num
    }
