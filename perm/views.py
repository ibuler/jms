# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from .forms import PermForm
from .models import Perm
from asset.models import Asset


def perm_list(request):
    perms = Perm.objects.all()
    form = PermForm()
    return render(request, 'perm/list.html', {'perms': perms, 'form': form})


@require_POST
def perm_add(request):
    form = PermForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('perm:list'))
    else:
        return HttpResponse('无效请求')


def perm_detail(request, perm_id):
    perm = get_object_or_404(Perm, id=perm_id)
    return render(request, 'perm/detail.html', {'perm': perm})


@require_POST
def perm_recycle(request):
    pass


@require_POST
def perm_del(request, perm_id):
    perm = get_object_or_404(Perm, id=perm_id)
    perm.delete()
    return HttpResponse('删除成功')