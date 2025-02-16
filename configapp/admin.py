from django.contrib import admin
from .models import Kurs, Student

class KursAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'get_course', 'created_at', 'updated_at')
    search_fields = ('full_name', 'kurs__title')
    list_filter = ('kurs',)

    @admin.display(description="Course")
    def get_course(self, obj):
        return obj.course.title

admin.site.register(Kurs, KursAdmin)
admin.site.register(Student, StudentAdmin)
