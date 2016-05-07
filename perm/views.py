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


def perm_detail(request, user_id):
    return render(request, 'perm/detail.html', {'user_id': user_id})


@require_POST
def perm_recycle(request):
    user_id = request.POST.get('user_id', '0')
    asset_id = request.POST.get('asset_id', '0')

    user = get_object_or_404(User, id=user_id)
    asset = get_object_or_404(Asset, id=asset_id)

    perms = Perm.objects.filter(user=user, asset=asset)
    for perm in perms:
        perm.user.remove(user)

    return HttpResponse('回收成功')


@require_POST
def perm_del(request):
    user_id = request.POST.get('id')
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Http404('删除失败')

    perms = user.perm_set.all()
    for perm in perms:
        perm.user.remove(user)

    return HttpResponse('清空成功')