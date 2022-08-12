from django.db import models

from datetime import datetime

from apps.users.models import BaseModel

class Course(BaseModel):
    name = models.CharField(verbose_name="course name", max_length=50)
    desc = models.CharField(verbose_name="course description", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="learning hours (in mins)")
    degree = models.CharField(verbose_name="difficulty level", choices=(("cj", "elementary level"), ("zj", "intermediate level"), ("gj", "advanced level")), max_length=2)
    students = models.IntegerField(default=0, verbose_name='student numbers')
    fav_nums = models.IntegerField(default=0, verbose_name='number of saved')
    click_nums = models.IntegerField(default=0, verbose_name="number of views")
    notice = models.CharField(verbose_name="course announcement", max_length=300, default="")
    category = models.CharField(default=u"Backend Development", max_length=20, verbose_name="course category")
    tag = models.CharField(default="", verbose_name="course tags", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="course notes")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="instructor words")

    detail = models.TextField(verbose_name="course details")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="cover pic", max_length=100)

    class Meta:
        verbose_name = "class info"
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    # on-delete:
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"chapter title")
    learn_time = models.IntegerField(default=0, verbose_name="learning hours in mins")

    class Meta:
        verbose_name = "lesson chapters"
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="chapter name", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="video name")
    learn_times = models.IntegerField(default=0, verbose_name="learning hours in mins")
    url = models.CharField(max_length=200, verbose_name="video url")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="name")
    file = models.FileField(upload_to="course/resource/%Y/%m", verbose_name= "download url", max_length=200)
    class Meta:
        verbose_name = " course resouces"
        verbose_name_plural = verbose_name