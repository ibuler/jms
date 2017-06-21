#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 

from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import User


class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'username': TextInput(attrs={'placeholder': 'username'}),
            'password': PasswordInput(attrs={'placeholder': 'password'}),
            'email': EmailInput(attrs={'placeholder': 'email'})
        }
