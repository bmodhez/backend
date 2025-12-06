from django.contrib import admin
from .models import User, LoginHistory


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name')
    ordering = ('email',)


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'login_time', 'ip_address', 'success', 'failure_reason')
    list_filter = ('success', 'login_time')
    search_fields = ('email', 'ip_address')
    ordering = ('-login_time',)
    readonly_fields = ('login_time',)
