from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book, Publisher, User, BookInstance, Genre


# Create your views here.
def index(request):
    a = Author.objects.all()
    b =  Book.objects.all()
    con = {a:b}
    for i in a:
        return HttpResponse((f"{i.id}.{i.name}"))

