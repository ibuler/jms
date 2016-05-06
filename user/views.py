from django.shortcuts import render


from django.contrib.auth.models import User

# Create your views here.


def user_add(request):
    return render(request, 'base.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {'users': users})
