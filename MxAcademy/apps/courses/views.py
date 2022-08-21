from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


from apps.courses.models import Course, CourseTag, CourseResource, Video
from apps.operations.models import UserFavorite, UserCourse, CourseComments


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """
        Get course details
        """
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        # #获取收藏状态
        # has_fav_course = False
        # has_fav_org = False
        # if request.user.is_authenticated:
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        #通过课程的tag做课程的推荐
        # tag = course.tag
        # related_courses = []
        # if tag:
        #     related_courses = Course.objects.filter(tag=tag).exclude(id__in=[course.id])[:3]

        # tags = course.coursetag_set.all()
        # tag_list = [tag.tag for tag in tags]
        #
        # course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
        # related_courses = set()
        # for course_tag in course_tags:
        #     related_courses.add(course_tag.course)

        return render(request, "course-detail.html", {
            "course":course,
            # "has_fav_course":has_fav_course,
            # "has_fav_org":has_fav_org,
            # "related_courses":related_courses
        })


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """get course list data"""
        all_courses = Course.objects.order_by("-created_time")
        hot_courses = Course.objects.order_by("-click_nums")[:3]

        #搜索关键词
        # keywords = request.GET.get("keywords", "")
        # s_type = "course"
        # if keywords:
        #     all_courses = all_courses.filter(Q(name__icontains=keywords)|Q(desc__icontains=keywords)|Q(desc__icontains=keywords))

        # Sorting courses
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-click_nums")

        # Pagination
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=1, request=request)
        courses = p.page(page)

        return render(request, "course-list.html", {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses,
            # "keywords":keywords,
            # "s_type":s_type
        })

