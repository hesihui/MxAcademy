from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from apps.operations.forms import UserFavForm, CommentsForm
from apps.operations.models import UserFavorite, CourseComments
from apps.courses.models import Course
from apps.organizations.models import CourseOrg, Teacher


class CommentView(View):
    def post(self, request, *args, **kwargs):
        """
        用户收藏，取消收藏
        """
        if not request.user.is_authenticated:
            return JsonResponse({
                "status":"fail",
                "msg":"用户未登录"
            })

        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            course = comment_form.cleaned_data["course"]
            comments = comment_form.cleaned_data["comments"]

            comment = CourseComments()
            comment.user = request.user
            comment.comments = comments
            comment.course = course
            comment.save()

            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "参数错误"
            })


class AddFavView(View):
    def post(self, request, *args, **kwargs):
        """
        User subscribe, user un-subscribe
        """

        # check if user is authenticated
        if not request.user.is_authenticated:
            return JsonResponse({
                "status": "fail",
                "msg": "User didn't login"
            })

        user_fav_form = UserFavForm(request.POST)
        if user_fav_form.is_valid():
            # get data from user_fav form
            fav_id = user_fav_form.cleaned_data["fav_id"]
            fav_type = user_fav_form.cleaned_data["fav_type"]

            # check if the user already subscribed the records
            existed_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
            if existed_records:
                # delete record from user favorite (user's personal data)
                existed_records.delete()
                # subtract the total fav counts from org, course, instructor
                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums -= 1
                    course_org.save()
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse({
                    "status": "success",
                    "msg": "Unsubscribed"
                })
            else:
                # create a new userFavorite obj for saving the new record
                user_fav = UserFavorite()
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.user = request.user
                user_fav.save()
                return JsonResponse({
                    "status": "success",
                    "msg": "Subscribed"
                })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "Parameter Error"
            })




