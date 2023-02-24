from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import NewUser


@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "real_id", "phone", "is_active"]
    list_editable = ["real_id"]
    search_fields = ["real_id", "phone", "email"]
    list_filter = ["is_active"]
    list_per_page = 10

