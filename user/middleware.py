#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginRequireMiddleware(object):
    def process_request(self, request):
        if request.path not in [reverse_lazy('user:login')]:
            if not request.user.is_authenticated:
                return redirect(reverse_lazy('user:login'))

if __name__ == '__main__':
    pass
