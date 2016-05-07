from django.shortcuts import render

from django.contrib.auth.models import User


def perm_list(request):
    users = User.objects.iterator()
    return render(request, 'perm/list.html', {'users': users})