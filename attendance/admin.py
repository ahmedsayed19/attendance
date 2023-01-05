from django.contrib import admin

from .models import Attendance, AttendanceAction
# Register your models here.
admin.site.register(Attendance)
admin.site.register(AttendanceAction)