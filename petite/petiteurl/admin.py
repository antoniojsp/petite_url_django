from django.contrib import admin
from .models import Urls
from django.template.defaultfilters import truncatechars  # or truncatewords


# Register your models here.
class MemberAdmin(admin.ModelAdmin):

    list_display = ("hash_value", "url", "date_added", "exp_date", "count")

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

admin.site.register(Urls, MemberAdmin)
