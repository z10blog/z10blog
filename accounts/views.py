from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import LoginForm


class LoginView(View):
    form_class = LoginForm
    initial = {'email': '输入您的电子邮件地址', 'password': 'password'}
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/admin/')
        return render(request, self.template_name, {'form': form})
