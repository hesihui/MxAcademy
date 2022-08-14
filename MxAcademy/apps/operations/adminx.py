import xadmin

from apps.operations.models import UserAsk, CourseComments, UserCourse, UserFavorite, UserMessage


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'created_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'created_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'created_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'created_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'created_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'created_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'created_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'created_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'created_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'created_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)