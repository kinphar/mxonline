from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})

