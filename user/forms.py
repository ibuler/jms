#!/usr/bin/env python
# coding: utf-8
# Created by guang on 
# 

from django.contrib.auth.models import User
from django import forms
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


class UserUpdateForm(ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'is_superuser', 'is_active']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            # 'password': PasswordInput(attrs={'placeholder': 'password'}),
            'email': EmailInput(attrs={'placeholder': 'email'})
        }
        labels = {
            'is_superuser': 'Is Admin'
        }
