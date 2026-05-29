from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse

from forum.models import Thread, Post, SiteSettings


class PostInline(admin.TabularInline):
    model = Post
    ordering = ('created',)

class ThreadAdmin(admin.ModelAdmin):
    inlines = (PostInline, )

admin.site.register(Thread, ThreadAdmin)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ('invite_code',)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj, _ = SiteSettings.objects.get_or_create(pk=1)
        return redirect(reverse('admin:forum_sitesettings_change', args=[obj.pk]))
