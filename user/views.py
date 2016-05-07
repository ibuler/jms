# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


from django.contrib.auth.models import User

from .forms import UserAddForm
from .utils import Bash, ServerUserManager

# Create your views here.


def user_add(request):
    form = UserAddForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user_in_server = ServerUserManager(Bash)
        ret, msg = user_in_server.present(username=username, password=password)
        if not ret:
            user.save()
            return HttpResponseRedirect(reverse('user:list'))
        else:
            user_in_server.absent(username)
            return HttpResponse(msg)
    else:
        return HttpResponse('验证失败')


def user_list(request):
    users = User.objects.all()
    form = UserAddForm()
    return render(request, 'user/list.html', {'users': users, 'form': form})
