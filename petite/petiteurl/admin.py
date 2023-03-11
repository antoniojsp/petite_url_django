from django.contrib import admin
from .models import Urls
from django.template.defaultfilters import truncatechars  # or truncatewords


# Register your models here.
class MemberAdmin(admin.ModelAdmin):

    list_display = ("hash_value", "url", "date_added", "exp_date", "count")

admin.site.register(Urls, MemberAdmin)
