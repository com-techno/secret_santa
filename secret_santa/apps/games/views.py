from django.shortcuts import render, redirect


def new(request):
    return render(request, 'games/new-number.html')


def create(request):
    pass


def game(request):
    pass
