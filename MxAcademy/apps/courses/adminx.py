import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = "MxAcademy Management System"
    site_footer = "MxAcademy Distant Learning"
   # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ["degree", "desc"]


class LessonAdmin(object):
    list_display = ['course', 'name', 'created_time']
    search_fields = ['course', 'name']
    # course__name : since course is a foreign key,
    # if you want to filter the property of foreign key, use __
    list_filter = ['course__name', 'name', 'created_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'created_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'created_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'created_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'created_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)