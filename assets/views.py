# coding: utf-8

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, View, UpdateView
from django.urls import reverse_lazy

from .forms import AssetForm
from .models import Asset
from users.mixins import LoginRequiredMixin


class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = "assets/list.html"


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm
    template_name = "assets/add.html"
    success_url = reverse_lazy("assets:list")


class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset
    template_name = "assets/detail.html"


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = "assets/update.html"
    success_url = reverse_lazy("assets:list")


class AssetDeleteView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        asset_id = self.kwargs.get("pk", 0)
        asset = get_object_or_404(Asset, id=asset_id)
        asset.delete()
        return HttpResponse('删除成功')
