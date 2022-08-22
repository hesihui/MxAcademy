from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import redis
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from apps.users.models import UserProfile
from apps.users.forms import UserInfoForm, UploadImageForm
from apps.users.forms import RegisterGetForm
from apps.users.forms import LoginForm


class UploadImageView(LoginRequiredMixin, View):
    login_url = "/login/"

    # def save_file(self, file):
    #     with open("C:/Users/Administrator/PycharmProjects/MxOnline/media/head_image/uploaded.jpg", "wb") as f:
    #         for chunk in file.chunks():
    #             f.write(chunk)

    def post(self, request, *args, **kwargs):
        # handle uploaded avatar
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "fail"
            })
        # files = request.FILES["image"]
        # self.save_file(files)


class UserInfoView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, *args, **kwargs):
        current_page = "info"
        captcha_form = RegisterGetForm()
        return render(request, "usercenter-info.html", {
            "captcha_form": captcha_form,
            "current_page": current_page
        })

    def post(self, request, *args, **kwargs):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return JsonResponse({
                "status":"success"
            })
        else:
            return JsonResponse(user_info_form.errors)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        next = request.GET.get("next", "")
        return render(request, "login.html", {
            "next": next
        })

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
        # check if user and password exist via user obj
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)
            if user is not None:
                # if user exists
                login(request, user)
                # after login, direct to the home page
                next = request.GET.get("next", "")
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse("index"))
            else:
                # if user does not exist
                return render(request, "login.html",
                              {"msg": "user or password is not matched", "login_form": login_form})
        else:
            # if login fails
            return render(request, "login.html", {"login_form": login_form})

