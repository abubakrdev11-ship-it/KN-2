from django.contrib import admin
from apps.user.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role')
    search_fields = ('email', 'username')
