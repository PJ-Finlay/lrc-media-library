from django.contrib import admin
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MediaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teacher_username=request.user)

    def has_change_permission(self, request, obj=None):
        return True

    list_display = ('title', 'language', 'teacher_username', 'course_name')
    list_filter = ('language','teacher_username','course_name')  

admin.site.register(Media, MediaAdmin)
