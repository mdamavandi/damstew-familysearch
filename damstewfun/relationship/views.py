# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Relationship, where you get the verbal description of your relationship (e.g. second cousin once removed) with another person on FamilySearch.org")
