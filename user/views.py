# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .forms import UserAddForm, UserUpdateForm
from .utils import Bash, ServerUserManager


@user_passes_test(lambda user: user.is_superuser)
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


@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_update(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'].strip()
            user = form.save(commit=False)
            if password:
                user.set_password(password)
                user_in_server = ServerUserManager(Bash)
                ret, msg = user_in_server.present(username=username, password=password)
                if ret:
                    return HttpResponse(msg)
            user.save()
            return HttpResponseRedirect(reverse('user:list'))
    form = UserUpdateForm(instance=user)
    return render(request, 'user/update.html', {'form': form})


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/detail.html', {'user': user})


def user_list(request):
    users = User.objects.all()
    form = UserAddForm()
    return render(request, 'user/list.html', {'users': users, 'form': form})


@login_required
@user_passes_test(lambda user: user.is_superuser)
def user_del(request, user_id):
    # user_id = request.POST.get('id')
    print('Is ajax: %s' % request.is_ajax())
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponse('删除成功')


def login_(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user:list'))
            else:
                error = '用户已禁用'
        else:
            error = '用户密码不正确'
    return render(request, 'user/login.html', {'error': error})


def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))
