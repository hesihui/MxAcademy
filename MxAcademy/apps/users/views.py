from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.models import UserProfile



class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if not user_name:
            return render(request, "login.html", {"msg": "Please enter your user name! "})
        if not password:
            return render(request, "login.html", {"msg": "Please enter your password! "})

        # check if user and password exist via user obj
        user = authenticate(username=user_name, password=password)
        if user is not None:
            # if user exists
            login(request, user)
            # after login, direct to the home page


            return HttpResponseRedirect(reverse("index"))
        else:
            # if user does not exist
            return render(request, "login.html", {"msg": "user or password is not matched"})

