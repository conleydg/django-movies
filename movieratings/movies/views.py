from django.http import HttpResponse
from django.shortcuts import render
from .models import Rater, Movie, Rating


def index(request):
    return HttpResponse("Hello, world. You're at the views index.")

def top_twenty(request):
    return HttpResponse("Hello, world. You're at the top twenty view.")

def users(request):
    return HttpResponse("Hello, world. You're at the users view.")
