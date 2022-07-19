from django.contrib import admin
from .models import Department, Role, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "department", "salary", "bonus", "role", "phone", "hire_date")


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role)
admin.site.register(Employee, EmployeeAdmin)
