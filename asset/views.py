# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .forms import AssetForm
from .models import Asset

# Create your views here.


def asset_list(request):
    form = AssetForm()
    assets = Asset.objects.all()
    return render(request, 'asset/list.html', {'form': form, 'assets': assets})


@require_POST
def asset_add(request):
    form = AssetForm(request.POST)
    if form.is_valid():
        asset = form.save()
        return redirect(reverse('asset:list'))
    else:
        return HttpResponse('输入非法')


@login_required
@require_POST
def asset_del(request):
    asset_id = request.POST.get('id')
    asset = get_object_or_404(Asset, id=asset_id)
    asset.delete()
    return HttpResponse('删除成功')
