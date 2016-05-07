# coding: utf-8

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from .forms import PermForm


def perm_list(request):
    users = User.objects.iterator()
    form = PermForm()
    return render(request, 'perm/list.html', {'users': users, 'form': form})


@require_POST
def perm_add(request):
    form = PermForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('perm:list'))
    else:
        return HttpResponse('无效请求')