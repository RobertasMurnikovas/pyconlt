from django.contrib import admin

from conference.models import Event
from presenters.models.presenter import Presenter


class EventInline(admin.TabularInline):
    """
    Inline to show options to choose events.
    """
    model = Event
    raw_id_fields = ("year",)


class PresenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    fieldsets = (
        (None, {
            'fields': ('user', 'active'),
        }),
        ('Personal Info', {
            'fields': ('name', 'image', 'bio', 'expertise')
        }),
        ('Social links', {
            'fields': ('linkedin_handle', 'twitter_handle', 'github_handle')
        })
    )
    inlines = (EventInline, )


admin.site.register(Presenter, PresenterAdmin)
