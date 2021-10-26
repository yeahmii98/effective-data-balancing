from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello Kakao Nips! This is Tech Ground.")
