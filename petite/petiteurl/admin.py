from django.contrib import admin
from .models import Urls


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("hash_value", "url", "added_date", "exp_date", "count")


admin.site.register(Urls, MemberAdmin)
