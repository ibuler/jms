# coding: utf-8

from django.views.decorators.http import require_POST
from django.http import HttpResponse, Http404
from django.views.generic import ListView, CreateView, DetailView, View
from django.views.generic.edit import SingleObjectMixin
from django.urls import reverse_lazy

from users.mixins import LoginRequiredMixin
from users.models import User
from .forms import PermForm
from .models import Perm


class PermListView(LoginRequiredMixin, ListView):
    model = Perm
    template_name = "perms/list.html"
    form = PermForm()

    def get_context_data(self, **kwargs):
        context = super(PermListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context


class PermCreateView(LoginRequiredMixin, CreateView):
    model = Perm
    form_class = PermForm
    success_url = reverse_lazy("perms:list")

    def get(self, request, *args, **kwargs):
        return HttpResponse("Method not support", status=405)

    def form_invalid(self, form):
        return HttpResponse(";".join(form.errors), status=400)


class PermDetailView(DetailView):
    model = Perm
    template_name = "perms/detail.html"


class PermDeleteView(SingleObjectMixin, View):
    model = Perm

    def post(self, request, *args, **kwargs):
        perm = self.get_object()
        perm.delete()
        return HttpResponse("删除成功")


