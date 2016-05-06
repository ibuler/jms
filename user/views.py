from django.shortcuts import render

# Create your views here.


def user_add(request):
    return render(request, 'base.html')