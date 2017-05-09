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

    list_display = ('title', 'language', 'teacher_username', 'course_name','get_url_link')
    list_filter = ('language','teacher_username','course_name')

    #Create clickable link for URL field
    def get_url_link(self, obj):
        url_base = 'http://media.lrc.cornell.edu/VOD/'
        return ('<a href="%s%s" target="_blank">%s</a>' % (url_base, obj.url, obj.url))
    get_url_link.short_description = 'Name'
    get_url_link.allow_tags = True

admin.site.register(Media, MediaAdmin)
