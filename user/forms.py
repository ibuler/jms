#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 

from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'password': PasswordInput(attrs={'placeholder': 'password'}),
            'email': EmailInput(attrs={'placeholder': 'email'})

        }