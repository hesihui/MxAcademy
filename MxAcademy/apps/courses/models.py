from django.db import models

from datetime import datetime

from apps.users.models import BaseModel
from apps.organizations.models import Teacher


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Instructor")
    name = models.CharField(verbose_name="Course Name", max_length=50)
    desc = models.CharField(verbose_name="Course Description", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="Learning Hours (in mins)")
    degree = models.CharField(verbose_name="Difficulty Level", choices=(("cj", "elementary level"), ("zj", "intermediate level"), ("gj", "advanced level")), max_length=2)
    students = models.IntegerField(default=0, verbose_name='Student Numbers')
    fav_nums = models.IntegerField(default=0, verbose_name='Number of Favorites')
    click_nums = models.IntegerField(default=0, verbose_name="Number of Views")
    notice = models.CharField(verbose_name="Course Announcement", max_length=300, default="")
    category = models.CharField(default=u"Backend Development", max_length=20, verbose_name="Course Category")
    tag = models.CharField(default="", verbose_name="Course Tags", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="Course Notes")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="Instructor Words")

    detail = models.TextField(verbose_name="Course Details")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="Cover Pic", max_length=100)

    class Meta:
        verbose_name = "Class Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    # on-delete:
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"Chapter Title")
    learn_time = models.IntegerField(default=0, verbose_name="Learning Hours in Mins")

    class Meta:
        verbose_name = "Lesson Chapters"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="Chapter Name", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Video Name")
    learn_times = models.IntegerField(default=0, verbose_name="Learning Hours in Mins")
    url = models.CharField(max_length=200, verbose_name="Video Url")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Course Name")
    file = models.FileField(upload_to="course/resource/%Y/%m", verbose_name= "Download Url", max_length=200)

    class Meta:
        verbose_name = "Course Resources"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name