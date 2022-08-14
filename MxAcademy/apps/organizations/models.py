from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name="City Name")
    desc = models.CharField(max_length=200, verbose_name="Description")

    class Meta:
        verbose_name = "city"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Course Organization Name")
    desc = models.TextField(verbose_name="Organization Description")
    tag = models.CharField(default="Most Popular", max_length=15, verbose_name="Organization Tag")
    category = models.CharField(default="pxjg", verbose_name="Organization Category", max_length=20,
                                choices=(("pxjg", "Bootcamp"), ("gr", "Personal Instructor"), ("gx", "University")))
    click_nums = models.IntegerField(default=0, verbose_name="Number of Views")
    fav_nums = models.IntegerField(default=0, verbose_name="Number of Favorite")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="Org Logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name="Org Address")
    students = models.IntegerField(default=0, verbose_name="Number of Students")
    course_nums = models.IntegerField(default=0, verbose_name="Number of Courses")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Currently Located City")

    class Meta:
        verbose_name = "Course Organization"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="Affiliated Org")
    name = models.CharField(max_length=50, verbose_name="Teacher Name")
    work_years = models.IntegerField(default=0, verbose_name="Teacher Working Years")
    work_company = models.CharField(max_length=50, verbose_name="Teacher Company")
    work_position = models.CharField(max_length=50, verbose_name="Teacher Title")
    points = models.CharField(max_length=50, verbose_name="Teacher Key Features")
    click_nums = models.IntegerField(default=0, verbose_name="Number of Views in Total")
    fav_nums = models.IntegerField(default=0, verbose_name="Number of Favorites in Total")
    age = models.IntegerField(default=18, verbose_name="Age")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="Avatar", max_length=100)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name