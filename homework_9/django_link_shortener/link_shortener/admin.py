from django.contrib import admin

from link_shortener.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('link',)
    list_display_links = ('link',)
    search_fields = ('link',)


admin.site.register(Link, LinkAdmin)
